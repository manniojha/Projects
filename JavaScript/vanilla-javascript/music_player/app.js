let apiResponse = new apiCalling();
let counter = 0;
let resultLength;
let isSelectedShuffle = false;
let isSelectedRepeat = false;

//Event Listener
function eventListner() {
  document.addEventListener("DOMContentLoaded", init);
}

//Calling Event Listener
eventListner();

//DOMContentLoaded
function init() {
  let id = 0;
  apiResponse.getAllDetails().then((results) => {
    const list = document.querySelector("#list");
    const result = results.playlist;
    resultLength = results.playlist.length;
    result.forEach((elem) => {
      list.innerHTML += `
        <div class="list-grid-element" id = ${id++} onclick="renderMusic(this)">
            <img src="${elem.albumCover}" class="list-grid-element-img" alt="">
            <div class = "list-grid-element-details">
                <h3 class="music-name">${elem.track}</h3>
                <p class="author-name">${elem.artist}</p>
            </div>
        </div>`;
    });
  });
  elementSelector(0);
}

function elementSelector(id) {
  apiResponse.getAllDetails().then((results) => {
    const playing = document.querySelector("#playing");
    const result = results.playlist[id];
    if (document.getElementsByClassName("playing-element") != null) {
      removeElementsByClass("playing-element");
    }
    playing.innerHTML += `
        <div class="playing-element">
        <audio src="${result.file}" class="playing-element-audio" id="player" controls></audio>
            <img src="${result.albumCover}" class="playing-element-img" alt="">
            <h3 class="playing-element-author-name">${result.artist} - ${result.track}</h3>
        </div>`;
  });
  setTimeout(play(), 500);
}

function removeElementsByClass(className) {
  var elements = document.getElementsByClassName(className);
  while (elements.length > 0) {
    elements[0].parentNode.removeChild(elements[0]);
  }
}

function play() {
  setTimeout(function () {
    document.getElementById("play").dispatchEvent(new Event("click"));
  }, 1000);
}

function previousMusic() {
  var playPause = document.getElementById("play");
  if (counter > 0) {
    counter--;
  }
  elementSelector(counter);
  playPause.className = "fa fa-play-circle fa-3";
}

function shuffler() {
  let elemShuffle = document.getElementById("shuffle-music");
  let elemRepeat = document.getElementById("repeat-music");

  isSelectedRepeat = false;
  elemRepeat.className = "fa fa-undo";

  if (isSelectedShuffle == false) {
    isSelectedShuffle = true;
    elemShuffle.className = "fa fa-random isSelected";
  } else {
    elemShuffle.className = "fa fa-random";
    isSelectedShuffle = false;
  }
  return;
}

function playMusic() {
  var playPause = document.getElementById("play");
  var player = document.getElementById("player");
  if (playPause.className === "fa fa-play-circle fa-3") {
    playPause.className = "fa fa-pause-circle fa-3";
    player.play();
    progressBar_Update();
  } else {
    playPause.className = "fa fa-play-circle fa-3";
    player.pause();
  }
}

function nextMusic() {
  var playPause = document.getElementById("play");
  if (counter == resultLength - 1) {
    counter = -1;
  }
  elementSelector(++counter);
  playPause.className = "fa fa-play-circle fa-3";
}

function repeat() {
  let elemShuffle = document.getElementById("shuffle-music");
  let elemRepeat = document.getElementById("repeat-music");

  isSelectedShuffle = false;
  elemShuffle.className = "fa fa-random";

  if (isSelectedRepeat == false) {
    isSelectedRepeat = true;
    elemRepeat.className = "fa fa-undo isSelected";
  } else {
    elemRepeat.className = "fa fa-undo";
    isSelectedRepeat = false;
  }
  return;
}

function renderMusic(element) {
  elementSelector(element.id);
  counter = element.id;
  var playPause = document.getElementById("play");
  if (playPause.className === "fa fa-pause-circle fa-3") {
    play();
  } else {
    play();
    play();
  }
}

function seek(element) {
  var player = document.getElementById("player");
  var offset = element.getBoundingClientRect();
  var totalWidth = offset.width;
  var percentage = element.onclick.arguments[0].offsetX / totalWidth;
  var audioTime = player.duration * percentage;
  player.currentTime = audioTime;
  var progressBar = document.getElementsByClassName("Song_Progress");
  progressBar[0].style.width =
    ((player.currentTime + 0.25) / player.duration) * 100 + "%";
}

function progressBar_Update() {
  var player = document.getElementById("player");
  player.addEventListener("timeupdate", function (event) {
    event.preventDefault();
    event.stopPropagation();
    var currentTime = player.currentTime;
    var duration = player.duration;
    var progressBar = document.getElementsByClassName("Song_Progress");
    progressBar[0].style.width = ((currentTime + 0.25) / duration) * 100 + "%";
  });

  player.addEventListener("ended", () => {
    document.getElementById("play").className = "fa fa-play-circle fa-3";
    var player = document.getElementById("player");
    if (isSelectedShuffle == true) {
      var elementId = Math.floor(Math.random() * resultLength);
      elementSelector(elementId);
      return;
    }
    if (isSelectedRepeat == true) {
      play();
      return;
    }
    elementSelector(++counter);
  });
}
