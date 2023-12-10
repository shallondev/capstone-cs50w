document.addEventListener('DOMContentLoaded', () => {
    console.log('DOMContentLoaded event fired');

    // Get elements
    var questions = document.querySelectorAll('.question');

    // Format question content
    questions.forEach(question => {
        question.innerHTML = formatQuestionContent(question.innerHTML);
    });

    // Helper function to format question content
    function formatQuestionContent(content) {
        // Modify the content using regular expressions
        content = content.replace(/(\([A-E]\))/g, '<br><br>$1');
        content = content.replace(/(\(i\))/g, '<br><br>$1');
        content = content.replace(/(\(ii\))/g, '<br>$1');
        content = content.replace(/(\(iii\))/g, '<br>$1');
        content = content.replace(/(\(iv\))/g, '<br>$1');
        content = content.replace(/(?<!\d)[.]\s/g, '$&<br>');
        content = content.replace(/\b(Calculate)\b/g, '<br>$1');
        return content;
    }
});
