export const API = {
    "BASE_API": "http://127.0.0.1:8000/api/tasks/",
   // "POST": detailRoute
 
}

export const detailRoute = (id) => {
    return API.BASE_API + `${id}/`
}

