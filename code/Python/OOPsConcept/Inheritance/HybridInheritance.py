# Create a Python program that demonstrates hybrid inheritance for a media content system. The program should involve the following classes:

# Base Class: Media :# Attributes: title (string): Title of the media content. # creator (string): Creator or producer of the media.
    # Methods:
        # display_media_info(): Display the title and creator of the media.
        # play(): Print a message indicating that the media is being played.
# Derived Class 1: Video (inherits from Media)

# Additional Attributes:
# resolution (string): The resolution of the video (e.g., 1080p, 4K).
# duration (int): Duration of the video in minutes.
# Methods:
# display_video_info(): Display the video details (title, creator, resolution, and duration).
# stream(): Print a message indicating that the video is being streamed.
# Derived Class 2: Audio (inherits from Media)

# Additional Attributes:
# bitrate (int): The audio bitrate in kbps.
# length (int): The length of the audio in minutes.
# Methods:
# display_audio_info(): Display the audio details (title, creator, bitrate, and length).
# play_audio(): Print a message indicating that the audio is being played.
# Derived Class 3: Movie (inherits from both Audio and Video)

# Additional Attributes:
# genre (string): The genre of the movie (e.g., action, drama).
# rating (float): The movie's rating (e.g., 4.5/5).
# Methods:
# display_movie_info(): Display the movie details (title, creator, bitrate, resolution, duration, genre, and rating).
# play_movie(): Print a message indicating that the movie is being played.

# class Media:
#     def __init__(self, title, creator):
#         self.title = title
#         self.creator = creator
#     def display_media_info(self):
#         print("Title: ", self.title)
#         print("Creator: ", self.creator)
#     def play(self):
#         print(f"The media '{self.title}' created by {self.creator} is being played.")
# class Video (Media):
#     def __init__(self, title, creator, resolution, duration):
#         Media.__init__(self,title, creator)
#         self.resolution = resolution
#         self.duration = duration
#     def display_video_info(self):
#         print("Title: ", self.title)
#         print("Creator: ", self.creator)
#         print("Resolution: ", self.resolution)
#         print("Duration: ", self.duration)
#     def stream(self):
#        print(f"The video '{self.title}' is being streamed in {self.resolution} resolution.")

# class Audio (Media):
#     def __init__(self,title, creator,bitrate,length):
#         Media.__init__(self,title, creator)
#         self.bitrate = bitrate
#         self.length = length
#     def display_audio_info(self):
#         print("Title: ", self.title)
#         print("Creator: ", self.creator)
#         print("Bitrate: ", self.bitrate)
#         print("Length: ", self.length)
#     def play_audio(self):
#        print(f"The audio '{self.title}' is being played at {self.bitrate} kbps.")

# class Movie(Audio, Video):
#     def __init__(self, title, creator, bitrate, length, resolution, duration, genre, rating):
#         Audio.__init__(self, title, creator, bitrate, length)
#         Video.__init__(self, title, creator, resolution, duration)
#         self.genre = genre
#         self.rating = rating

#     def display_movie_info(self):
#         print("\nMovie Info:")
#         print(f"Title: {self.title}")
#         print(f"Creator: {self.creator}")
#         print(f"Bitrate: {self.bitrate} kbps")
#         print(f"Length: {self.length} minutes")
#         print(f"Resolution: {self.resolution}")
#         print(f"Duration: {self.duration} minutes")
#         print(f"Genre: {self.genre}")
#         print(f"Rating: {self.rating}/5")

#     def play_movie(self):
#         print(f"The movie '{self.title}' of genre '{self.genre}' is being played with a rating of {self.rating}/5.")

# movie = Movie("Inception","Christopher Nolan",320,148,"4K",148,"Sci-Fi",4.8)
# movie.display_movie_info()
# movie.play_movie()


# class university: (university_name)

# college  (collage_name, location)

# branch (branch_name)

# student(student_name, reg_no)

class university:
    def __init__(self,university_name):
        self.university_name = university_name

class college(university):
    def __init__(self,university_name, collage_name, location):
        university.__init__(self,university_name)
        self.collage_name = collage_name
        self.location = location

class branch(university):
    def __init__(self,university_name,branch_name):
        university.__init__(self,university_name)
        self.branch_name = branch_name

class student(college,branch):
    def __init__(self,university_name, collage_name, location,branch_name,student_name, reg_no):
        college.__init__(self,university_name, collage_name, location)
        branch.__init__(self,university_name,branch_name)
        self.student_name = student_name
        self.reg_no = reg_no
    def display(self):
        print("\nStudent Info:")
        print(f"Student Name: {self.student_name}")
        print(f"Registration No: {self.reg_no}")
        print(f"Branch Name: {self.branch_name}")
        print(f"Collage Name: {self.collage_name}")
        print(f"Location: {self.location}")
        print(f"University Name: {self.university_name}")


student1 = student(
    university_name="Cochin University of Science and Technology (CUSAT)",
    collage_name="School of Engineering, Cochin University",
    location="Cochin, Kerala",
    branch_name="Mechanical Engineering",
    student_name="Manu Mathew",
    reg_no="CUSAT2024002"
)
student1.display()

