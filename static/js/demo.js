var areanamechart = dc.barChart("#areadiv");
var genchart = dc.rowChart("#gendiv");
var chart = dc.pieChart("#test");
var speedchart = dc.pieChart("#speed");
var timechart = dc.pieChart("#timediv");
var weatherchart = dc.pieChart("#weatherdiv");

d3.csv("t2.csv",function(err,data){
if (err) throw err;

var ndx = crossfilter(data);
var all = ndx.groupAll();

//dimension
var areaname = ndx.dimension(function(d){
  return d["area"];
});

var timech = ndx.dimension(function (d){
  return d["time"];
})
var piespeedchart = ndx.dimension(function(d){
  return d["speed"];
})
var piechartgender = ndx.dimension(function (d){
  return d["Gender"];
});

var gen = ndx.dimension(function(d){
  return d["causeofaccidents"];
});

var weatherdime = ndx.dimension(function(d){
  return d["Weather"];
});

//group here...
var areatypegroup = areaname.group();
var gentypegroup = gen.group();
var piechofgen =  piechartgender.group();
var piechofspeed = piespeedchart.group();
var timegroup = timech.group();
var weathergroup = weatherdime.group();


areanamechart
    .width(1000)
        .height(400)
        .x(d3.scale.ordinal())
        .xUnits(dc.units.ordinal)
        .brushOn(false)
        .xAxisLabel('Area')
        .yAxisLabel('Number of Accidents in city')
        .dimension(areaname)
        .barPadding(0.1)
        .outerPadding(0.05)
        .group(areatypegroup);

  genchart
  .width(550)
  .height(350)
  .dimension(gen)
  .group(gentypegroup)
  .elasticX(true);

chart.
  width(420)
  .height(250)
  .innerRadius(50)
  .dimension(piechartgender)
  .group(piechofgen)
  .legend(dc.legend())
  .on('pretransition', function(chart) {
      chart.selectAll('text.pie-slice').text(function(d) {
          return d.data.key + ' ' + dc.utils.printSingleValue((d.endAngle - d.startAngle) / (2*Math.PI) * 100) + '%';
      })
  });

speedchart
    .width(500)
    .height(250)
    .innerRadius(50)
    .dimension(piespeedchart)
    .group(piechofspeed)
    .legend(dc.legend())
    .on('pretransition', function(chart) {
         chart.selectAll('text.pie-slice').text(function(d) {
            return d.data.key + ' ' + dc.utils.printSingleValue((d.endAngle - d.startAngle) / (2*Math.PI) * 100) + '%';
        })
    });
timechart
    .width(500)
    .height(300)
    .innerRadius(20)
    .externalLabels(30)
    .externalRadiusPadding(40)
    .drawPaths(true)
    .dimension(timech)
    .group(timegroup)
    .legend(dc.legend())
    .on('pretransition', function(chart) {
                chart.selectAll('.dc-legend-item text')
                .text('')
                .append('tspan')
                .text(function(d) { return d.name; })
                .append('tspan')
                .attr('x', 120)
                .attr('text-anchor', 'end')
                .text(function(d) { return d.time; });
            });

  weatherchart
      .dimension(weatherdime)
      .group(weathergroup)
      .width(500)
    .height(300)
    .innerRadius(20)
    .externalLabels(30)
    .externalRadiusPadding(40)
    .drawPaths(true)
    .legend(dc.legend())
    .on('pretransition', function(chart) {
         chart.selectAll('text.pie-slice').text(function(d) {
            return d.data.key + ' ' + dc.utils.printSingleValue((d.endAngle - d.startAngle) / (2*Math.PI) * 100) + '%';
        })
    });

dc.renderAll();
});
