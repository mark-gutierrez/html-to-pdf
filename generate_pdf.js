const puppeteer = require("puppeteer");
const fs = require("fs");
const PDFDocument = require("pdfkit");

// (async () => {
//     const browser = await puppeteer.launch();
//     const page = await browser.newPage();

//     // Load your HTML file with JavaScript
//     await page.goto(
//         "file:///C:/Users/markg/Downloads/pdf/side_by_side_plots.html",
//         {
//             waitUntil: "networkidle0", // Wait for all network requests to finish
//         }
//     );

//     // Capture a screenshot of the rendered page
//     const screenshot = await page.screenshot();

//     // Create a PDF using pdfkit
//     const pdfDoc = new PDFDocument();
//     pdfDoc.pipe(fs.createWriteStream("output.pdf"));
//     pdfDoc.image(screenshot, 0, 0, { width: 600 }); // You may need to adjust the width

//     pdfDoc.end();

//     await browser.close();
// })();

(async () => {
    // Launch a headless browser
    const browser = await puppeteer.launch();

    // Create a new page
    const page = await browser.newPage();

    // Set the viewport size (optional)
    await page.setViewport({ width: 800, height: 600 });

    // Navigate to your HTML file
    await page.goto(
        "file:///C:/Users/markg/Downloads/pdf/side_by_side_plots.html",
        {
            waitUntil: "networkidle0", // Wait for all network requests to finish
        }
    );

    // Wait for a few seconds (optional)
    await page.waitForTimeout(2000);

    // Generate a PDF from the rendered HTML
    await page.pdf({ path: "output.pdf", format: "A4" });

    // Close the browser
    await browser.close();

    console.log("PDF generated as output.pdf");
})();
