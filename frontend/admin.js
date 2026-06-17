const API_URL = "http://127.0.0.1:8000";

document.getElementById("education-form").addEventListener("submit", async function(event) {
    event.preventDefault();

    const endYearValue = document.getElementById("end_year").value;

    const education = {
        degree: document.getElementById("degree").value,
        institution: document.getElementById("institution").value,
        start_year: Number(document.getElementById("start_year").value),
        end_year: endYearValue ? Number(endYearValue) : null,
        description: document.getElementById("description").value,
        projects: []
    };

    try {
        const response = await fetch(`${API_URL}/education/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(education)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        await response.json();

        document.getElementById("message").textContent =
            "Formation ajoutée avec succès.";

        document.getElementById("education-form").reset();

    } catch (error) {
        document.getElementById("message").textContent =
            "Erreur lors de l'ajout.";

        console.error("Erreur lors de l'ajout de la formation :", error);
    }
});