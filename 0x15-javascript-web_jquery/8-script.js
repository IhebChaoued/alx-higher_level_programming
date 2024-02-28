$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function(data) {
        var movies = data.results;
        
        var $listMovies = $('UL#list_movies');
        movies.forEach(function(movie) {
            $listMovies.append('<li>' + movie.title + '</li>');
        });
    }
});
