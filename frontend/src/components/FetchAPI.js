//FetchApi.js

//import axios from "axios";
    
async function fetchSkins() {
    const { data } = await fetch('http://0.0.0.0:80/skins/web')
    console.log(data)
    return data.json()
}
    
export default fetchSkins;