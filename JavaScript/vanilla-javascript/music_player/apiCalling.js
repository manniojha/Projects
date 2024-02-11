 class apiCalling{

    async getAllDetails(){

        let apiResponse = await fetch('https://5dd1894f15bbc2001448d28e.mockapi.io/playlist');
        let playlist = await apiResponse.json();
        return {
            playlist
         }
    }
}