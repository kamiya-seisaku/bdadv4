const fs = require('fs');
const path = require('path');

const listFilePath = 'filelist.txt';  // Your .gitignore-style list
const outputFilePath = 'concatenated.js'; // Output file
const rootFolder = 'c:\\codes\\bdadv4';  // Your project root

async function concatenateFiles() {
  const filesToConcatenate = await fs.promises.readFile(listFilePath, 'utf-8')
    .then(data => data.split('\n').map(line => line.trim()).filter(line => line && !line.startsWith('#'))); // Ignore comments and empty lines

  const outputContent = [];

  // Generate folder structure
  outputContent.push(`[folder structure]`);
  outputContent.push(`(root: "${rootFolder}")`);
  const visitedFolders = new Set(); // Track to avoid duplicate folders
  for (const file of filesToConcatenate) {
    const relativePath = path.relative(rootFolder, file);
    const folderPath = path.dirname(relativePath);
    const parts = folderPath.split(path.sep);
    for (let i = 0; i < parts.length; i++) {
      const partialPath = parts.slice(0, i + 1).join(path.sep);
      if (!visitedFolders.has(partialPath)) {
        outputContent.push(`${'  '.repeat(i)}L[${parts[i]}]`); // Indentation based on depth
        visitedFolders.add(partialPath);
      }
    }
  }

  // Read and append file contents
  for (const file of filesToConcatenate) {
    const relativePath = path.relative(rootFolder, file);
    const content = await fs.promises.readFile(file, 'utf-8');
    outputContent.push(`\n["${relativePath}" codes]`);
    outputContent.push(content);
  }

  await fs.promises.writeFile(outputFilePath, outputContent.join('\n'));
  console.log('Concatenation complete!');
}

concatenateFiles().catch(err => console.error('Error:', err)); 
