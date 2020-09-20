<template>
    <v-row style="height: 85%">
        <v-col ref="chartdiv" >        
        </v-col>
    </v-row>
</template>

<script>
import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import am4themes_material from "@amcharts/amcharts4/themes/material";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";
import axios from 'axios';

am4core.useTheme(am4themes_material);
am4core.useTheme(am4themes_animated);

export default {
    name: 'Chart',
    props: ["idObject"],
    data: () => ({
        name: ''
    }),
    methods: {
        calculate: function(date){
            var a = date + 32044;
            var b = Math.floor(((4*a) + 3)/146097);
            var c = a - Math.floor((146097*b)/4);
            var d = Math.floor(((4*c) + 3)/1461);
            var e = c - Math.floor((1461 * d)/4);
            var f = Math.floor(((5*e) + 2)/153);

            var D = e + 1 - Math.floor(((153*f) + 2)/5);
            var M = f + 3 - 12 - Math.round(f/10);
            var Y = (100*b) + d - 4800 + Math.floor(f/10);

            return new Date(Y,M,D);
        },
        jdToDate: function(data){
            for (const dato in data){
                var a = dato.date + 32044;
            var b = Math.floor(((4*a) + 3)/146097);
            var c = a - Math.floor((146097*b)/4);
            var d = Math.floor(((4*c) + 3)/1461);
            var e = c - Math.floor((1461 * d)/4);
            var f = Math.floor(((5*e) + 2)/153);

            var D = e + 1 - Math.floor(((153*f) + 2)/5);
            var M = f + 3 - 12 - Math.round(f/10);
            var Y = (100*b) + d - 4800 + Math.floor(f/10);

            dato.date =  new Date(Y,M,D);
            }
        },
    },
    created(){
        this.name = 'http://35.247.220.23/' + this.idObject
    },
    mounted(){
        axios.get(this.name).
        then(res => {
            let chart = am4core.create(this.$refs.chartdiv, am4charts.XYChart);
            
            chart.data = res.data;

            for(var i=0; i<res.data.length; i++){

                var a = res.data[i].date + 32044;
                var b = Math.floor(((4*a) + 3)/146097);
                var c = a - Math.floor((146097*b)/4);
                var d = Math.floor(((4*c) + 3)/1461);
                var e = c - Math.floor((1461 * d)/4);
                var f = Math.floor(((5*e) + 2)/153);

                var D = e + 1 - Math.floor(((153*f) + 2)/5);
                var M = f + 3 - 12 - Math.round(f/10);
                var Y = (100*b) + d - 4800 + Math.floor(f/10);
                res.data[i].date = new Date(Y,M,D);
            }
            
            let dateAxis = chart.xAxes.push(new am4charts.DateAxis());
            dateAxis.dataFields.category = "date";

            let valueAxis = chart.yAxes.push(new am4charts.ValueAxis());

            let series = chart.series.push(new am4charts.LineSeries());
            series.dataFields.dateX = "date";
            series.dataFields.valueY = "valor";
            series.tooltipText = "magpsf: {valueY.value} error:{error}"

            let errorBullet = series.bullets.create(am4charts.ErrorBullet);
            errorBullet.isDynamic = true;
            errorBullet.strokeWidth = 2;

            let circle = errorBullet.createChild(am4core.Circle);
            circle.radius = 3;
            circle.fill = am4core.color("#ffffff");

            errorBullet.adapter.add("pixelHeight", function (pixelHeight, target) {
            let dataItem = target.dataItem;

            if(dataItem){
                let value = dataItem.valueY;
                let errorTopValue = value + dataItem.dataContext.error / 2;
                let errorTopY = valueAxis.valueToPoint(errorTopValue).y;

                let errorBottomValue = value - dataItem.dataContext.error / 2;
                let errorBottomY = valueAxis.valueToPoint(errorBottomValue).y;

                return Math.abs(errorTopY - errorBottomY);
            }
            return pixelHeight;
            })

            chart.cursor = new am4charts.XYCursor();
        }).catch(
            e => {
                console.log(e.response);
            }
        );
    
      
    }


}
</script>