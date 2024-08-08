document.addEventListener('DOMContentLoaded', () => {
    console.log('JavaScript is working!');

    window.showForm = function(formType) {
        const clientForm = document.getElementById('client-form');
        const driverForm = document.getElementById('driver-form');
        
        if (formType === 'client') {
            clientForm.style.display = 'block';
            driverForm.style.display = 'none';
        } else if (formType === 'driver') {
            clientForm.style.display = 'none';
            driverForm.style.display = 'block';
        }
    }
});
