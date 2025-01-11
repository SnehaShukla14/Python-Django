document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        const username = document.querySelector('input[name="username"]');
        const password = document.querySelector('input[name="password"]');
        
        // Basic client-side validation for empty fields
        if (!username.value || !password.value) {
            event.preventDefault();
            alert('Please fill out all fields');
        }
    });
});
