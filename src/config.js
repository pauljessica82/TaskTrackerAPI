export const API = {
    "BASE_API": "https://jessiecodes-reminderapp.herokuapp.com/api/tasks/",
}

export const detailRoute = (id) => {
    return API.BASE_API + `${id}/`
}

