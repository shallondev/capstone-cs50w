document.addEventListener("DOMContentLoaded", function () {
    // Assuming content is your string
    var questions = document.querySelectorAll('.question');
  
    questions.forEach(function (question) {
      // Add <br> before '(A)' or 'A.'
      question.innerHTML = question.innerHTML.replace(/(\(A\)|A\.)/g, "<br><br>$1");

      question.innerHTML = question.innerHTML.replace(/(\sCalculate)/g, "<br><br>$1");

      question.innerHTML = question.innerHTML.replace(/\s(iv\)|\(iv\))/g, "<br><br>$1");
      question.innerHTML = question.innerHTML.replace(/\s(i\)|\(i\))/g, "<br><br>$1");
      question.innerHTML = question.innerHTML.replace(/\s(ii\)|\(ii\))/g, "<br><br>$1");
      question.innerHTML = question.innerHTML.replace(/\s(iii\)|\(iii\))/g, "<br><br>$1");

    });
  });
  
  document.addEventListener("DOMContentLoaded", function () {
    var timeElement = document.getElementById('examTime'); // using ID instead of class
    var examTime = parseInt(timeElement.dataset.time, 10);
  
    function updateTimer() {
      var minutes = Math.floor(examTime / 60);
      var seconds = examTime % 60;
      var formattedTime = minutes + ":" + (seconds < 10 ? "0" : "") + seconds;
      timeElement.textContent = "Time Left: " + formattedTime;
  
      if (examTime > 0) {
        examTime--;
      } else {
        clearInterval(timerInterval);
        timeElement.textContent = "Time's up!";
      }
    }
  
    // Initial call to set the initial time
    updateTimer();
  
    // Update the timer every minute (60,000 milliseconds)
    var timerInterval = setInterval(updateTimer, 60000);
  });
  