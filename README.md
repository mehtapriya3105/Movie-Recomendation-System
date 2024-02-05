# Movie Recommendation System README

Welcome to the Movie Recommendation System based on the MovieLens dataset! This application leverages MongoDB to provide personalized movie recommendations through a user-friendly interface.

## Project Structure:

- **Frontend (React):**
  - A lightweight React application is employed to ensure fast loading times, emphasizing its one-time page loading feature.

- **Backend (FastAPI):**
  - FastAPI handles HTTP requests from the frontend, serving as a bridge between the user interface and the recommendation engine.

- **Recommendation Engine (recommendation_logic.py):**
  - The core recommendation logic is implemented in `recommendation_logic.py`. It utilizes a content-based filtering algorithm to generate movie recommendations based on the user's input.

- **Data Handling:**
  - Data is fetched from the MongoDB database using `data_reading.py`.
  - Data cleaning is performed by `data_cleaning.py` to ensure the quality of the information used by the recommendation engine.

- **Data Writing (data_writing.py):**
  - An optional `data_writing.py` file is provided to facilitate the writing of data into the MongoDB database, allowing for the addition of new information.

## Workflow:

1. **User Input:**
   - Users provide a movie name through the user interface.

2. **Frontend to Backend:**
   - The frontend sends an HTTP request to the FastAPI backend.

3. **Backend Processing:**
   - FastAPI processes the request and redirects the movie name to the `recommendation_logic.py` file.

4. **Recommendation Logic:**
   - The recommendation engine in `recommendation_logic.py` utilizes content-based filtering to generate movie recommendations.

5. **Data Handling:**
   - Cleaned data is fetched from the MongoDB database using `data_reading.py` to ensure accurate and relevant recommendations.

6. **User Receives Recommendations:**
   - The user receives a list of movie recommendations based on the input provided.

## Running the Application:

1. Ensure MongoDB is installed and running.
2. Adjust the MongoDB connection settings in `data_reading.py` and `data_writing.py` if needed.
3. Install required Python packages using `pip install -r requirements.txt`.
4. Run the FastAPI backend using `uvicorn main:app --reload`.
5. Start the React frontend using `npm start`.
6. Access the application at `http://localhost:3000` in your browser.

Feel free to explore and enhance the application based on your requirements. Enjoy personalized movie recommendations!