function openModal(location, distance, time, price) {
    document.getElementById('clientLocation').textContent = location;
    document.getElementById('rideDistance').textContent = distance;
    document.getElementById('estimatedTime').textContent = time;
    document.getElementById('ridePrice').textContent = price;
    document.getElementById('rideDetailsModal').style.display = 'block';
}

function closeModal() {
    document.getElementById('rideDetailsModal').style.display = 'none';
}

function confirmRide() {
    // Implement the functionality to confirm the ride here
    alert('Ride confirmed!');
    closeModal();
}

// Close the modal if the user clicks outside of the modal content
window.onclick = function(event) {
    if (event.target == document.getElementById('rideDetailsModal')) {
        closeModal();
    }
}
