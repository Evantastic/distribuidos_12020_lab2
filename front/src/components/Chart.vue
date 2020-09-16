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

am4core.useTheme(am4themes_material);
am4core.useTheme(am4themes_animated);

export default {
    name: 'Chart',
    mounted(){
      let chart = am4core.create(this.$refs.chartdiv, am4charts.XYChart);
      chart.data =[{
          "date": new Date(2020,0,20),
          "magsp": 1000,
          "error": 100
      },
      {
          "date": new Date(2020,0,21),
          "magsp": 2000,
          "error": 100
      },
      {
          "date": new Date(2020,0,22),
          "magsp": 3000,
          "error": 100
      },
      {
          "date": new Date(2020,0,23),
          "magsp": 4000,
          "error": 100
      },
      {
          "date": new Date(2020,0,24),
          "magsp": 5000,
          "error": 100
      },
      {
          "date": new Date(2020,0,25),
          "magsp": 6000,
          "error": 100
      },
      {
          "date": new Date(2020,0,26),
          "magsp": 7000,
          "error": 100
      },
      {
          "date": new Date(2020,0,27),
          "magsp": 8000,
          "error": 100
      },
      {
          "date": new Date(2020,0,28),
          "magsp": 9000,
          "error": 100
      },
      {
          "date": new Date(2020,0,29),
          "magsp": 10000,
          "error": 100
      },
      {
          "date": new Date(2020,0,30),
          "magsp": 9000,
          "error": 100
      },
      {
          "date": new Date(2020,0,31),
          "magsp": 8000,
          "error": 100
      },
      {
          "date": new Date(2020,1,1),
          "magsp": 7000,
          "error": 100
      },
      {
          "date": new Date(2020,1,2),
          "magsp": 6000,
          "error": 100
      },
      {
          "date": new Date(2020,1,3),
          "magsp": 5000,
          "error": 100
      },
      {
          "date": new Date(2020,1,4),
          "magsp": 6000,
          "error": 100
      },
      {
          "date": new Date(2020,1,5),
          "magsp": 7000,
          "error": 100
      },
      {
          "date": new Date(2020,1,6),
          "magsp": 8000,
          "error": 100
      },];
  
     /* let categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
      categoryAxis.renderer.grid.template.location = 0;
      categoryAxis.dataFields.category = "date";
      categoryAxis.renderer.minGridDistance = 60;*/

      let dateAxis = chart.xAxes.push(new am4charts.DateAxis());
      dateAxis.dataFields.category = "date";

      let valueAxis = chart.yAxes.push(new am4charts.ValueAxis());

      let series = chart.series.push(new am4charts.LineSeries());
      series.dataFields.dateX = "date";
      series.dataFields.valueY = "magsp";
      series.tooltipText = "{valueY.value} error:{error}"

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
      
    }


}
</script>