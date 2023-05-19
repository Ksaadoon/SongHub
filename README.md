# Songhub: Track your favorite songs:

The original idea for this application was to provide a list of artists with their respective albums. The home page lists a music catalog that is created progressively by any registered user. 
Only registered users can edit the music catalog.

Each registred user can select among the music catalog, the songs they want to favorite inside their personal account. 
A song can be favorited by many users, and many users can favorite the same song.

The application will be deployed on Heroku.

## Development environment:
SongHub is using Python3, Django (4.2.1), PostGresql stack.

### requirement.txt:
asgiref==3.6.0

Django==4.2.1

psycopg2-binary==2.9.6

sqlparse==0.4.4

## Database:

### Models and relationships:

The models have the following relationships:

* Artist and Album: The Artist model has a one-to-many relationship with the Album model. An artist can have multiple albums, but each album belongs to only one artist. This is represented by the foreign key field artist in the Album model, which references the Artist model.

* Album and Song: The Album model also has a one-to-many relationship with the Song model. An album can have multiple songs, but each song belongs to only one album. This is represented by the foreign key field album in the Song model, which references the Album model.

* User and FavoriteSong: The User model has a one-to-many relationship with the FavoriteSong model. A user can have multiple favorite songs, but each favorite song belongs to only one user. This is represented by the foreign key field user in the FavoriteSong model, which references the User model.

* FavoriteSong and Song: The FavoriteSong model has a many-to-many relationship with the Song model. A favorite song can be associated with multiple songs, and a song can be associated with multiple favorite songs. This is represented by the songs field in the FavoriteSong model, which is a ManyToManyField referencing the Song model.

In summary, an Artist can have multiple Albums, an Album can have multiple Songs, a User can have multiple FavoriteSongs, and a FavoriteSong can hold and be associated with multiple Songs.

### Diagram:

<a href="https://imgbox.com/DVURJ1aF" target="_blank"><img src="https://thumbs2.imgbox.com/76/c8/DVURJ1aF_t.png" alt="image host"/></a>

## Improvements:
1. Make it look prettier
2. Be able to add more than one song at the time when adding to the music catalog (pending)
3. Be able to delete an entry in the music catalog (album and its songs) and an artist. Understand how to manage the dependencies if a song is favorited.
4. Showing on the home page, how many users like the same song and who.





