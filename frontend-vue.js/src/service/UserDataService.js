import axios from 'axios'


const USER_API_URL = 'http://localhost:5000/api/v1'


class UserDataService {


    retrieveAllMedicos() {
        return axios.get(`${USER_API_URL}/medicos`);
    }

    retrieveAllHospitais() {
        return axios.get(`${USER_API_URL}/hospitais`);
    }

    retrieveAllPacs() {

        return axios.get(`${USER_API_URL}/pac`);
    }


    retrievePac(id) {

        return axios.get(`${USER_API_URL}/pac/${id}`);
    }


    deletePac(id) {

        return axios.delete(`${USER_API_URL}/pac/${id}`);
    }

    visualizarPac(id) {

        return axios.get(`${USER_API_URL}/pac/${id}/visualizar`);
    }

    updatePac(id, pac) {

        return axios.put(`${USER_API_URL}/pac/${id}`, pac);
    }


    createPac(pac) {

        return axios.post(`${USER_API_URL}/pac`, pac);
    }

}

export default new UserDataService()