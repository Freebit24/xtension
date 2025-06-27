const profileSelect = document.getElementById('profileSelect');
const authInput = document.getElementById('auth');
const ct0Input = document.getElementById('ct0');
const output = document.getElementById('output');
const addBtn = document.getElementById('addProfileBtn');
const deleteBtn = document.getElementById('deleteProfileBtn');

function loadProfiles() {
  const profiles = JSON.parse(localStorage.getItem('profiles') || '{}');

  // Ensure default "Me" profile exists
  if (!profiles["Me"]) {
    profiles["Me"] = { auth_token: '', ct0: '' };
    localStorage.setItem('profiles', JSON.stringify(profiles));
  }

  // Clear and populate the select box
  profileSelect.innerHTML = '';
  for (const name in profiles) {
    const option = document.createElement('option');
    option.value = name;
    option.textContent = name;
    profileSelect.appendChild(option);
  }

  loadSelectedProfile();
}

function loadSelectedProfile() {
  const profiles = JSON.parse(localStorage.getItem('profiles') || '{}');
  const selected = profileSelect.value;
  if (profiles[selected]) {
    authInput.value = profiles[selected].auth_token;
    ct0Input.value = profiles[selected].ct0;
  }
}

profileSelect.addEventListener('change', loadSelectedProfile);

document.getElementById('submit').onclick = async () => {
  const auth_token = authInput.value;
  const ct0 = ct0Input.value;

  const res = await fetch('http://localhost:5000/fetch-feed', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ auth_token, ct0 })
  });

  const data = await res.json();
  output.innerHTML = '';

  if (data.tweet_links && data.tweet_links.length > 0) {
    data.tweet_links.forEach(link => {
      const a = document.createElement('a');
      a.href = link;
      a.target = '_blank';
      a.textContent = link;
      output.appendChild(a);
    });
  } else {
    output.textContent = 'No tweets found.';
  }
};

addBtn.onclick = () => {
  const name = prompt("Enter profile name:");
  if (!name) return;

  const auth_token = authInput.value;
  const ct0 = ct0Input.value;

  const profiles = JSON.parse(localStorage.getItem('profiles') || '{}');
  profiles[name] = { auth_token, ct0 };
  localStorage.setItem('profiles', JSON.stringify(profiles));

  loadProfiles();
  profileSelect.value = name;
  alert(`Profile "${name}" added!`);
};

deleteBtn.onclick = () => {
  const selected = profileSelect.value;
  if (selected === "Me") {
    alert("Default profile cannot be deleted.");
    return;
  }

  const confirmDelete = confirm(`Are you sure you want to delete "${selected}"?`);
  if (!confirmDelete) return;

  const profiles = JSON.parse(localStorage.getItem('profiles') || '{}');
  delete profiles[selected];
  localStorage.setItem('profiles', JSON.stringify(profiles));

  loadProfiles();
  alert(`Profile "${selected}" deleted.`);
};

// Load everything on page load
loadProfiles();
