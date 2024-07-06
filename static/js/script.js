console.log('script.js loaded');

(function () {
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
                    if (xhr.readyState === 4) {
                        console.log('Response received:', xhr.responseText); // Log the response text
                        if (xhr.status === 200) {
                            try {
                                const response = JSON.parse(xhr.responseText);
                                if (response.redirect_url) {
                                    window.location.href = response.redirect_url;
                                } else {
                                    console.log('No redirect URL found in the response');
                                }
                            } catch (e) {
                                console.error('Failed to parse JSON response:', e);
                            }
                        } else {
                            console.error('Server responded with status:', xhr.status);
                            console.error('Response text:', xhr.responseText);
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

document.addEventListener('DOMContentLoaded', function () {
    const arrivalDateField = document.getElementById('id_arrival_date');
    const numberOfNightsField = document.getElementById('id_number_of_nights');

    arrivalDateField.addEventListener('change', function () {
        const date = new Date(arrivalDateField.value);
        const day = date.getUTCDay();

        let options = [];

        if (day === 1) { // Monday
            options = [4, 7];
        } else if (day === 5) { // Friday
            options = [2, 3, 7];
        }

        numberOfNightsField.innerHTML = '';
        options.forEach(function (option) {
            const opt = document.createElement('option');
            opt.value = option;
            opt.innerHTML = option;
            numberOfNightsField.appendChild(opt);
        });
    });
});