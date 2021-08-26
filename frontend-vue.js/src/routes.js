import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

const router = new Router({ 
    mode: 'history',
    routes: [
        {
            path: "/",
            name: "FormLista",
            component: () => import("./components/FormLista"),
        },
        {
            path: "/pac/:id",
            name: "Paciente",
            component: () => import("./components/FormMed"),
        },
        {
            path: "/pac/:id/visualizar",
            name: "Visualizacao",
            component: () => import("./components/FormVisualizacao"),
        },
    ]
});

export default router;