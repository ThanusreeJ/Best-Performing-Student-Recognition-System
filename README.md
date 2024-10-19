# Best-Performing-Student-Recognition-System
The **Best-Performing Student Recognition System** is basically dynamic identification and presentation of top performers based on multiple academic and extracurricular metrics. The system implements the web interface via Flask to allow users to input new student data, with recalculations running in real time.

**Implemented Key Features**

__Dynamic Data Input:__

We built a UI where one can insert new student information, including all their performance metrics on academics using a web form.
The data is then stored in a CSV file and always kept in a format which ensures a new entry for calculation of top performers
Top students calculation
The system computes the top three students based on an overall ranking score for a chosen batch year given an array of criteria such as GPA, consistency, and hackathons among others.
This involves reading through the CSV data, processing it, and updating the results dynamically on the page.

__User-friendly Interface:__
 
HTML and CSS was used in designing the front-end, thus the experience of using it intuitive to the user. However, a user is expected to choose a batch year and see who were the top three students according to the structured table format.

__Error Handling:__

Many mechanisms of error handling were also incorporated to make it robust. Data types were also handled and problems in reading the CSV file avoided.
Technical Stack

__Backend:__ Python with Flask handling all the request and data operations.

__Frontend:__ HTML for structuring, CSS for styling, and JavaScript for interaction purposes.

__Data Storage:__ CSV files for maintaining student records with easy modification and access.

__THE OUTPUT IMAGE__
![OUTPUT](https://github.com/ThanusreeJ/Best-Performing-Student-Recognition-System/raw/main/output.png)
