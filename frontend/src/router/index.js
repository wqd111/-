import Vue from 'vue'

import Router from 'vue-router'

const routerOptions = [

{ path: '/', component: 'Home' , name:"Home", meta: { navShow: false}},
{ path: "/login",component: 'Login', name:"Login", meta: { navShow: false}},
{ path: "/register",component: 'Register', name:"Register", meta: { navShow: false}},
{ path: "/mainwindow",component: 'MainWindow', name:"MainWindow", meta: { navShow: true}},
{ path: "/echart",component: 'Echart', name:"Echart", meta: { navShow: true}},
{ path: "/disease", component: 'Disease', name: "Disease", meta: { navShow: true } },
{ path: "/drug", component: 'Drug', name: "Drug", meta: { navShow: true } },
{ path: "/indication", component: 'Indication', name: "Indication", meta: { navShow: true } },
{ path: "/contra", component: 'Contraindication', name: "Contraindication", meta: { navShow: true } },
{ path: "/addnode",component: 'AddNode', name:"AddNode", meta: { navShow: true}},
{ path: "/addrelation",component: 'AddRelation', name:"AddRelation", meta: { navShow: true}},
{ path: "/ingraph", component: 'IndicationGraph', name: "IndicationGraph", meta: { navShow: true } },
{ path: "/contragraph", component: 'ContraGraph', name: "ContraGraph", meta: { navShow: true } },
{ path: "/manage", component: 'Manage', name: "Manage", meta: { navShow: true } },
{ path: "/allgraph", component: 'AllGraph', name: "AllGraph", meta: { navShow: true } },
{ path: "/combgraph", component: 'CombGraph', name: "CombGraph", meta: { navShow: true } },
{ path: "/druggraph", component: 'DrugGraph', name: "DrugGraph", meta: { navShow: true } },
{ path: "/guide", component: 'GuideManage', name: "GuideManage", meta: { navShow: true } },

]

const routes = routerOptions.map(route => {

return {

...route,

component: () => import(`@/components/${route.component}.vue`)

}

})

Vue.use(Router)

export default new Router({

routes,

mode: 'history'

})
