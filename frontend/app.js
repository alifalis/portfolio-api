const API_URL = "http://127.0.0.1:8000";

async function loadEducation() {
    const container = document.getElementById("education-list");

    try {
        const response = await fetch(`${API_URL}/education/`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const educations = await response.json();
        container.innerHTML = "";
        educations.forEach(education => {
            const card =document.createElement("div");
            card.className = "bg-white p-4 rounded shadow";
             card.innerHTML = `
            
                <h3 class="text-xl font-bold">
                    ${education.degree}
                </h3>

                <p class="text-gray-700">
                    ${education.institution}
                </p>

                <p>
                    ${education.start_year} -
                    ${education.end_year ?? "Aujourd'hui"}
                </p>


                <p class="mt-2">
                    ${education.description}
                </p>


                <h4 class="font-semibold mt-3">
                    Projets :
                </h4>


                <ul class="list-disc ml-6">

                    ${
                        education.projects.map(project => `
                            <li>
                                <strong>
                                    ${project.title}
                                </strong>

                                : ${project.description}
                            </li>
                        `).join("")
                    }

                </ul>
            `;


            // Ajoute la carte créée dans la page HTML
            container.appendChild(card);
        });


            

    } catch (error) {
        console.error('Error loading education data:', error);
        container.innerHTML = '<p>Erreur lors du chargement des formations.</p>';
    }

}
loadEducation();