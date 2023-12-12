document.addEventListener("DOMContentLoaded", function () {
    var timeElement = document.getElementById('examTime');
    var examTime = parseInt(timeElement.dataset.time, 10) * 60;
    var form = document.getElementById('takeExamID');

    // Get exam ID from the hidden div
    var examIdContainer = document.getElementById('examIdContainer');
    var examId = parseInt(examIdContainer.dataset.examId, 10);
    var redirectUrl = `/exam_summary/${examId}/`;

    function updateTimer() {
        var minutes = Math.floor(examTime / 60);
        var seconds = examTime % 60;
        var formattedTime = minutes + ":" + (seconds < 10 ? "0" : "") + seconds;
        timeElement.textContent = "Time Left: " + formattedTime;

        //change font
        timeElement.style.fontSize = "32px";


        var timeIntervals = [3600, 1800, 900, 600, 300, 60];

        if (timeIntervals.includes(examTime)) {
            alert(formatAlertMessage(examTime));
        }

        if (examTime > 0) {
            examTime--;
        } else {
            clearInterval(timerInterval);
            timeElement.textContent = "Time's up! Submitting the form...";

            // Submit the form
            form.submit();

            // Redirect the user
            window.location.href = redirectUrl;
        }
    }

    function formatAlertMessage(timeInSeconds) {
        var minutes = Math.floor(timeInSeconds / 60);
        var seconds = timeInSeconds % 60;
        return minutes + " minute(s) and " + seconds + " second(s) left!";
    }

    updateTimer();
    var timerInterval = setInterval(updateTimer, 1000);

    
});