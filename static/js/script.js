console.log('script.js loaded');

(function () {
    // Initialize EmailJS with your public key
    emailjs.init("tDN0tUMP56E9wc3Dc");
})();

window.onload = function () {
    document.getElementById('res-form').addEventListener('submit', function (event) {
        event.preventDefault();

        const form = this;

        // Send email with EmailJS
        emailjs.sendForm('service_2kin33p', 'reservation_noti', form)
            .then(() => {
                console.log('Email sent successfully!');

                // AJAX request to submit form data to the server
                const xhr = new XMLHttpRequest();
                xhr.open("POST", form.action, true);
                xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
                xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
                xhr.onreadystatechange = function () {
                    if (xhr.readyState === 4 && xhr.status === 200) {
                        const response = JSON.parse(xhr.responseText);
                        if (response.redirect_url) {
                            // Redirect to the room detail page upon success
                            window.location.href = response.redirect_url;
                        } else {
                            console.log('No redirect URL found in the response');
                        }
                    }
                };
                const formData = new FormData(form);
                const data = new URLSearchParams(formData).toString();
                xhr.send(data);
            }, (error) => {
                console.log('Email sending failed...', error);
                alert('Failed to send reservation request. Please try again later.');
            });
    });
};