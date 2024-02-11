import "./App.css";
import Rows from "./Components/Rows";
import Banner from "./Components/Banner";
import Requests from "./Helpers/request";
import Nav from "./Components/Nav";

function App() {
  return (
    <div className="App">
      <Nav />
      <Banner />

      <Rows
        title="NETFLIX ORIGINALS"
        fetchUrl={Requests.fetchNetflixOriginals}
        isLargeRow
      />
      <Rows title="Trending Now" fetchUrl={Requests.fetchTrending} />
      <Rows title="Top Rated" fetchUrl={Requests.fewtchTopRated} />
      <Rows title="Action Movie " fetchUrl={Requests.fetchActionMovies} />
      <Rows title="Comdey Movie" fetchUrl={Requests.fetchComedyMovies} />
      <Rows title="Horror Movie" fetchUrl={Requests.fetchHorrorMovies} />
      <Rows title="Romance Movie" fetchUrl={Requests.fetchRomanceMovies} />
      <Rows title="Documentaries" fetchUrl={Requests.fetchDocumentaries} />
    </div>
  );
}

export default App;
