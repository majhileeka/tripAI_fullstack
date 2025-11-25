document.getElementById("tripForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const budget = parseFloat(document.getElementById("budget").value);
  const days = parseInt(document.getElementById("days").value);
  const type = document.getElementById("type").value;

  const data = { budget, days, type };
  const results = document.getElementById("results");
  results.innerHTML = "<p>⏳ Generating your trip plan...</p>";

  try {
    const response = await fetch("https://tripai-backend.onrender.com/api/plan_trip", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });
    const trip = await response.json();

    if (trip.error) throw new Error(trip.error);

    results.innerHTML = `
      <h2>Destination: ${trip.destination}</h2>
      <h3>Flights:</h3>
      <ul>${trip.flights.map(f => `<li>${f}</li>`).join("")}</ul>
      <h3>Hotels:</h3>
      <ul>${trip.hotels.map(h => `<li>${h}</li>`).join("")}</ul>
      <h3>Itinerary:</h3>
      <ul>${trip.itinerary.map(i => `<li>Day ${i.day}: ${i.activity}</li>`).join("")}</ul>
      <a href="${trip.map_link}" target="_blank">🌐 View 3D Map</a>
    `;
  } catch (err) {
    results.innerHTML = `<p style="color:red;">Error: ${err.message}</p>`;
  }
});
