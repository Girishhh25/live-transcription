const { ipcRenderer } = require('electron');

document.addEventListener('DOMContentLoaded', () => {
  const transcriptionsDiv = document.getElementById('transcriptions');
  
  if (!transcriptionsDiv) {
    console.error('Transcriptions div not found');
    return;
  }

  // Example: Add received transcriptions to UI
  ipcRenderer.on('new-transcription', (event, text) => {
    const p = document.createElement('p');
    p.textContent = text;
    transcriptionsDiv.appendChild(p);
  });
});
