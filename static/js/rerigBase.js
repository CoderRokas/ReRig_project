function goHome() {
    window.location = '/';
} 

function goToAbout() {
    window.location = '/rerig/about/';
}

function goToSearch() {
    window.location = '/rerig/search/';
}

function goToAccount(username) {
    window.location = '/rerig/account/'+ username;
}

function goToPost(id) {
    console.log(id)
    window.location = '/rerig/post/' + String(id);
}

function goToLogin() {
    window.location = '/rerig/login/';
}

function logout() {
    window.location = '/rerig/logout';
}

function register() {
    window.location = '/rerig/register/';
}

function goToAddPost() {
    window.location = '/rerig/add_post';
}