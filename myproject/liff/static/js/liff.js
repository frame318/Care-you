async function getFriendship() {
  const friend = await liff.getFriendship()
  if (!friend.friendFlag) {
    if (confirm("คุณยังไม่ได้เพิ่ม Bot เป็นเพื่อน จะเพิ่มเลยไหม?")) {
      window.location = "https://line.me/R/ti/p/@701lwdym"
    }
  }
}
async function getUserProfile() {
  const profile = await liff.getProfile()
  document.getElementById("userId").value = profile.userId;
}
async function main() {
  liff.ready.then(() => {
    if (liff.isLoggedIn()) {
      getFriendship()
      getUserProfile()
    } else {
      liff.login({ redirectUri:'https://care-you-django-project.herokuapp.com/index' })
      // liff.login()
    }
  })
  await liff.init({ liffId: "1654982439-PGQy8pvw" })
}
main()
