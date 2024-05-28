console.log('script.js loaded');

(function () {
    // https://dashboard.emailjs.com/admin/account
    emailjs.init({
        publicKey: "tDN0tUMP56E9wc3Dc",
    });
})();

window.onload = function () {
    document.getElementById('res-form').addEventListener('submit', function (event) {
        event.preventDefault();
        // these IDs from the previous steps
        emailjs.sendForm('reservation_noti', this)
            .then(() => {
                console.log('SUCCESS!');
            }, (error) => {
                console.log('FAILED...', error);
            });
    });
}