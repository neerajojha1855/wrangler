import {jsPDF} from 'jsPDF';

export function generatePackingList(city, items) {
    const pdf = new jsPDF();

    pdf.setFont("timesnewroman", "bold");

    pdf.setFontSize(22);
    pdf.text("[Wrangler : Survival Matrix]", 20, 20);

    pdf.setFontSize(14);
    pdf.text(`Destination: ${city}`, 20, 35);

    pdf.setFontSize(12);
    pdf.setFont("timesnewroman", "normal");

    let yPos = 50;
    items.forEach(item => {
        pdf.text(`[ ] ${item}`, 20, yPos);
        yPos += 10;
    });

    pdf.text("Generated Securely // Structure the Chaos", 20, 280);

    pdf.save(`wrangler_packlist_${city.replace(' ', '_')}.pdf`);
}