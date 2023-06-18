include <parameters.scad>;

module simple_stand(location=[0.0,0.0,0.0],rotation=0.0) {
    translate(location) {
        rotate([0,0,rotation]){
            difference()
            {
                cylinder(h=standHeight+standLipHeight,
                    r=standRadius+standLipWidth,
                    center=false);
                translate([0,0,standHeight]) {
                    cylinder(h=standHeight+standLipHeight,
                            r=standRadius,
                            center=false);
                }
                translate([0,0,-(standLipHeight/2.0)]) {
                    cylinder(h=standHeight+standLipHeight,
                            r=standHoleRadius,
                            center=false);
                }
            }
        }
    }
}
module next_layer(bottom_z=2.0){
    translate([0.0,0.0,bottom_z]){
        rotate([0,0,45.0]){
            union(){
                difference(){
                    cylinder(h=3,r=61,center=false);
                    cylinder(h=9,r=59,center=true);
                    }
                simple_stand(location=[standLocationRadius,0,0],rotation=0);
                simple_stand(location=[0,standLocationRadius,0],rotation=-90);
                simple_stand(location=[-standLocationRadius,0,0],rotation=180);
                simple_stand(location=[0,-standLocationRadius,0],rotation=90);
            }
        }
    }
}

//projection(cut=true) {
translate(0.0,0.0,-(2+StandHeight)){
next_layer(0);
}
//}