document.addEventListener('DOMContentLoaded', function() {
    var forgotPasswordBtn = document.getElementById('forgotPasswordBtn');
    if (forgotPasswordBtn) {
        forgotPasswordBtn.addEventListener('click', function() {
            window.location.href = '/forgot-password-request/';
        });
    }

    var createAccountBtn = document.getElementById('createAccountBtn');
    if (createAccountBtn) {
        createAccountBtn.addEventListener('click', function() {
            window.location.href = '/register/';
        });
    }
});