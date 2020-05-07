<template>
    <div>
        <div class='breadcrumb'>
            <el-breadcrumb separator="/" class="bc">
                <el-breadcrumb-item :to="{ path: '/mainwindow' }">首页</el-breadcrumb-item>
                <el-breadcrumb-item>适应证知识图谱</el-breadcrumb-item>
                <router-link :to="{name: 'MainWindow'}">
                    <el-button round size="mini" class="back-btn">返回</el-button>
                </router-link>
            </el-breadcrumb>
        </div>
        <div class='disease_title'>
            <p>适应证图谱</p>
            <div class='table-btn'>
                <router-link to='/indication'>
                    <el-button type="primary" size="medium">查看表格</el-button>
                </router-link>
            </div>
        </div>
        <div class="btn">
            <el-button type='primary' size='medium' @click="clickbtn()">查看图谱</el-button>
        </div>
        <div class="echart_box">
            <div id="container" style="width:100%; height:100%;"></div>
        </div>
        
        
        
    </div>
    
</template>

<script type="text/javascript">

import axios from 'axios'
import echarts from 'echarts'

export default {
    //注册组件
    data(){
        return{
            myChart:null,
            chartData:[],
            chartlink:[],
            search:false
            
        }
    },
    mounted(){
        this.drawChart(searchVal);
    },

    methods:{
        drawChart(searchVal){
            
            const path = `http://localhost:5000/graph/query/indication`
            axios
            .get(path,{params:{
                table:'indication',
                msg: searchVal
            }})
            .then(response => {
                
                this.chartData = response.data.nodes_data;
                this.chartLink = response.data.links_data;
                
            })
            .catch(error => {
                console.log(error)
            })

            // var datae = this.chartData;
            // var datal = this.chartLink;



            let dom = document.getElementById("container");
            this.myChart= echarts.init(dom);
            // this.chartData=this.dataEChart();
            // this.chartLink=this.linkEChart();

            let option={
                tooltip:{
                    formatter: function(x) {
                        if (x.data.category != undefined){
                            if(x.data.category == 1){
                                return '药品类型：'+x.data.name;
                            }else if(x.data.category == 2){
                                return '疾病：'+x.data.name;
                            }
                            else{
                                return '人群：'+x.data.name;
                            }
                        }
                        else{
                            return '适应证：'+x.data.value;
                        }
                        
                    }
                },
                animationDurationUpdate: 1500,
                animationEasingUpdate: 'quinticInOut',
                
                series: [
                    {
                        categories: [{
                name: '药品类型',
                itemStyle: {
                    normal: {
                        color: "#DC143C",
                    }
                }
            }, {
                name: '人群',
                itemStyle: {
                    normal: {
                        color: "#4592FF",
                    }
                }
            }, {
                name: '疾病',
                itemStyle: {
                    normal: {
                        color: "#FFA500",
                    }
                }
            }],
                        
                        edgeLabel: {
                            normal: {
                                formatter: "{c}",
                                show: true,
                            }
                        },
                        edgeSympol:'circle',
                        force:{
                            repulsion:100,
                            gravity:0.03,
                            edgeLength:80,
                            layoutAnimation : true

                        },
                        edgeSymbolSize: [4, 50],
                        edgeLabel: {
                            normal: {
                                show: true,
                                textStyle: {
                                    fontSize: 10
                                },
                                formatter: "{c}"
                            }
                        },
                        draggable: true,
                        lineStyle: {
                            normal: {
                                opacity: 0.9,
                                width: 1,
                                curveness: 0
                            }
                        },
                        layout:'force',
                        roam:true,
                        focusNodeAdjacency: true,
                
                        itemStyle:{
                            normal:{
                                color: '#6495ED'
                            },
                //鼠标放上去有阴影效果
                            emphasis: {
                            shadowColor: '#3721db',
                            shadowOffsetX: 0,
                            shadowOffsetY: 0,
                            shadowBlur: 40,
                            },
                        },
                        label:{
                            normal:{
                                show:true
                            }
                        },
                        type:'graph',
                        links: this.chartLink,
                        data: this.chartData
                }]
            };
            this.myChart.setOption(option);
            this.myChart.on('click', function (params) {
                console.log(params.data)//获取点击的头像的数据信息
            });
        },
        clickbtn(){
            this.search = true;
            var searchVal = this.search;
            
            this.drawChart(searchVal);
        }
        // dataEChart(){
        //     let data=[
        //         {
        //         name: '左心室肥厚',
        //         symbolSize: 76,
        //         id:'1'
        //     }, {
        //         name: '稳定性冠心病',
        //         symbolSize: 76,
        //         id:'2'
        //     }, {
        //         name: '心肌梗死后',
        //         symbolSize: 76,
        //         id:'3'
        //     }, {
        //         name: '心力衰竭',
        //         symbolSize: 76,
        //         id:'4'
        //     }, {
        //         name: '心房颤动预防',
        //         symbolSize: 76,
        //         id:'5'
        //     }, {
        //         name: '脑血管病',
        //         symbolSize: 76,
        //         id:'6'
        //     }, {
        //         name: '颈动脉内中膜增厚',
        //         symbolSize: 76,
        //         id:'7'
        //     }, {
        //         name: '蛋白尿/微量白蛋白尿',
        //         symbolSize: 76,
        //         id:'8'
        //     }, {
        //         name: '肾功能不全',
        //         symbolSize: 76,
        //         id:'9'
        //     }, {
        //         name: '糖尿病',
        //         symbolSize: 76,
        //         id:'10'
        //     }, {
        //         name: '血脂异常',
        //         symbolSize: 76,
        //         id:'11'
        //     }, {
        //         name: 'CCB',
        //         symbolSize: 76,
        //         category: 0,
        //         id:'12'
        //     }, {
        //         name: 'ACEI',
        //         symbolSize: 76,
        //         category: 0,
        //         id:'13'
        //     }, {
        //         name: 'ARB',
        //         symbolSize: 76,
        //         category: 0,
        //         id:'14'
        //     }, {
        //         name: '利尿剂',
        //         symbolSize: 76,
        //         category: 0,
        //         id:'15'
        //     }, {
        //         name: 'β受体阻滞剂',
        //         symbolSize: 76,
        //         category: 0,
        //         id:'16'
        //     }
        //     ];
        //     return data;
        // },
        // linkEChart(){
        //     let dataLink=[
        //         {value: "适应证+",source: "1",target: "12"},
        //         {value: "适应证+",source: "1",target: "13"},
        //         {value: "适应证+",source: "1",target: "14"},
        //         {value: "适应证+",source: "2",target: "12"},
        //         {value: "适应证+",source: "2",target: "13"},
        //         {value: "适应证+",source: "2",target: "14"},
        //         {value: "适应证+",source: "2",target: "16"},
        //         {value: "适应证+",source: "3",target: "13"},
        //         {value: "适应证+",source: "3",target: "14"},
        //         {value: "适应证+",source: "3",target: "15"},
        //         {value: "适应证+",source: "3",target: "16"},
        //         {value: "适应证+",source: "4",target: "13"},
        //         {value: "适应证+",source: "4",target: "14"},
        //         {value: "适应证+",source: "4",target: "15"},
        //         {value: "适应证+",source: "4",target: "16"},
        //         {value: "适应证+",source: "5",target: "13"},
        //         {value: "适应证+",source: "5",target: "14"},
        //         {value: "适应证+",source: "6",target: "12"},
        //         {value: "适应证+",source: "6",target: "13"},
        //         {value: "适应证+",source: "6",target: "14"},
        //         {value: "适应证+",source: "6",target: "15"},
        //         {value: "适应证+",source: "7",target: "12"},
        //         {value: "适应证+",source: "8",target: "13"},
        //         {value: "适应证+",source: "8",target: "14"},
        //         {value: "适应证+",source: "9",target: "13"},
        //         {value: "适应证+",source: "9",target: "14"},
        //         {value: "适应证+",source: "9",target: "15"},
        //         {value: "适应证+",source: "10",target: "13"},
        //         {value: "适应证+",source: "10",target: "14"},
        //         {value: "适应证+",source: "11",target: "13"},
        //         {value: "适应证+",source: "11",target: "14"},

        //         {value: "适应证-",source: "2",target: "15"},
        //         {value: "适应证-",source: "3",target: "12"},
        //         {value: "适应证-",source: "4",target: "12"},
        //         {value: "适应证-",source: "5",target: "12"},
        //         {value: "适应证-",source: "5",target: "15"},
        //         {value: "适应证-",source: "5",target: "16"},
        //         {value: "适应证-",source: "7",target: "15"},
        //         {value: "适应证-",source: "7",target: "16"},
        //         {value: "适应证-",source: "8",target: "12"},
        //         {value: "适应证-",source: "8",target: "15"},
        //         {value: "适应证-",source: "8",target: "16"},
        //         {value: "适应证-",source: "9",target: "16"},
        //         {value: "适应证-",source: "10",target: "16"},
        //         {value: "适应证-",source: "11",target: "15"},
        //         {value: "适应证-",source: "11",target: "16"},
                
        //         {value: "适应证±",source: "1",target: "15"},
        //         {value: "适应证±",source: "1",target: "16"},
        //         {value: "适应证±",source: "6",target: "16"},
        //         {value: "适应证±",source: "7",target: "13"},
        //         {value: "适应证±",source: "7",target: "14"},
        //         {value: "适应证±",source: "9",target: "12"},
        //         {value: "适应证±",source: "10",target: "12"},
        //         {value: "适应证±",source: "10",target: "15"},
        //         {value: "适应证±",source: "11",target: "12"},
        //     ]
        //     return dataLink;

        // },



            

        // handleEdit(index, row) {
        //     console.log(index, row);
        // },
        // handleDelete(index, row) {
        //     console.log(index, row);
        // },
        // getMongo(search) {
        //     const path = `http://localhost:5000/mongo/query`

        //     axios
        //     .get(path,{
        //         params:{
        //             table: "disease",
        //             msg: search
        //         }
        //     })
        //     .then(response => {
        //         var is_success = response.data.code
        //         if(is_success == 200){
        //             this.tableData = response.data.data
        //         }
        //         else{
        //             alert(response.data.msg)
        //             this.tableData = []
        //         }
                
        //     })
        //     .catch(error => {
        //         console.log(error)
        //     })
        // },
        // search_disease(){
        //     var search = this.searchVal;
        //     this.getMongo(search);
            /* if (search){
                
            } */
        // }
        
    }
    
}
</script>
<style type="text/css">
.echart_box{
    width:100%;
    height:800px;
    margin-top:50px;
    margin-bottom:200px;

}
.table-btn{
    float:right;
    margin-right:250px;
    position:relative;
    top:-50px;
}
.disease_title{
    font-size: 32px;
    font-weight: bold;
    text-align: left;
    margin-left:13%;
    margin-top:100px;
}
.disease_search{
    width:74%;
    margin-left:13%;
    margin-top:40px;
    
}

.disease_input{
    float:left;
    height:30px;
    width:200px;
    margin-top:5px;
}

.disease_table{
    margin-left: 13%;
    margin-top:100px;
    
}

.add_btn{
    float: right;
    margin-left:100%;
}

#search_btn{
    float:left;
    margin-left:10px;
}
.breadcrumb{
    margin-left:10%;
    width: 80%;
    height:50px;
    margin-top:-25px;
    border-left: 1px solid LightSteelBlue;
    border-bottom: 1px solid LightSteelBlue;
    border-right: 1px solid LightSteelBlue;
}

.bc{
    margin-left:20px;
    padding-top:20px;
    
}

.back-btn{
    margin-left:80%;
    margin-top:-2%;
}
.btn{
    position:relative;
    top:-44px;
    left:500px;
    width:50px;

}

</style>

