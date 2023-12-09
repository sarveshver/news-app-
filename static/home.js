function postComment(event, form) {
    console.log('Form Element:', form);
    event.preventDefault();

    // Get the form data
    const formData = new FormData(form);

    // Retrieve the index from the form
    const index = form.dataset.index;

    // Send the comment asynchronously using AJAX
    fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest', // Add this header to identify AJAX requests
        },
    })
    .then(response => response.json())
    .then(data => {
        // Update the comments section with the new comment
        const commentsSection = document.getElementById(`comments-${index}`);
        const newComment = document.createElement('div');
        newComment.innerHTML = `
            <p>${data.user_name} - ${data.created_at}</p>
            <p>${data.comment_text}</p>
            <hr>
        `;
        commentsSection.appendChild(newComment);

        // Clear the form
        form.reset();
    })
    .catch(error => console.error('Error posting comment:', error));
    document.addEventListener('DOMContentLoaded', function () {
        const commentButtons = document.querySelectorAll('.post-comment');
        commentButtons.forEach(button => {
            button.addEventListener('click', function (event) {
                const form = document.forms['commentForm' + this.dataset.index];
                postComment(event, form);
            });
        });
    });
    
}
