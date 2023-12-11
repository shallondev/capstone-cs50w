document.addEventListener('DOMContentLoaded', () => {
    console.log('Script is running');

    // Get elements
    var questionContents = document.querySelectorAll('.question-content');

    // Format question content
    questionContents.forEach(content => {
        content.innerHTML = formatQuestionContent(content.innerHTML);
    });

    function formatQuestionContent(content) {
        console.log('Formatting content:', content);
    
        // Add line breaks after Roman numerals and certain patterns
        content = content.replace(/(\([A-E]\))/g, '<br><br>$1');
        content = content.replace(/(\(?[ivxlc]+\))/ig, '<br>$1');
        
        // Add line breaks after certain patterns
        content = content.replace(/(?<![A-Z\d])[.]\s/g, '$&<br>');
        
        // Separate 'Calculate' from the following text
        content = content.replace(/\b(Calculate)\b/g, '<br>$1');
    
        console.log('Formatted content:', content);
        return content;
    }
    
});



