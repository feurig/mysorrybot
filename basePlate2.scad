include <parameters.scad>;


module screw_head(location=[0.0,0.0,0.0],rotation=0.0) {
    translate(location) {
 //       rotate([0,0,rotation]){
            cylinder(h=6,
                    r1=standRadius*2,
                    r2=standHoleRadius/3,
                    center=true);
 //       }
    }
}

module base_plate(){
    difference(){
        cylinder(r=62,h=2,center=false);
        union(){
            translate([14,0,0]){
                translate([-69.0,0,0]){cylinder(r=standHoleRadius,h=standHoleDepth,center=true);}

                translate([-60,0,0]){cube([10,40,standHoleDepth],center=true);}
                translate([-30,0,0]){cube([sensorLength,sensorWidth,standHoleDepth],center=true);}
                translate([0,0,0]) { cube([18,28,standHoleDepth],center=true);}
                translate([0,49,0]) { cube([28,8,standHoleDepth],center=true);}
                translate([0,-49,0]) { cube([28,8,standHoleDepth],center=true);}
                translate([4.5,20,0]){cylinder(r=standHoleRadius,h=standHoleDepth,center=true);}
                translate([4.5,38,0]){cylinder(r=standHoleRadius,h=standHoleDepth,center=true);}
                translate([4.5,-20,0]){cylinder(r=standHoleRadius,h=standHoleDepth,center=true);}
                translate([4.5,-38,0]){cylinder(r=standHoleRadius,h=standHoleDepth,center=true);}
                translate([-37.5,0,0]){cylinder(r=standHoleRadius,h=standHoleDepth,center=true);}
                translate([-12, 22.5,0]){cylinder(r=standHoleRadius,h=standHoleDepth,center=true);}
                translate([-12,-22.5,0]){cylinder(r=standHoleRadius,h=standHoleDepth,center=true);}
            }
    
            rotate([0,0,45.0]){
                union(){
                    screw_head(location=[standLocationRadius,0,0],rotation=0);
                    screw_head(location=[0,standLocationRadius,0],rotation=-90);
                    screw_head(location=[-standLocationRadius,0,0],rotation=180);
                    screw_head(location=[0,-standLocationRadius,0],rotation=90);
                }
            }
            rotate([0,0,45.0]){
                union(){
                    screw_head(location=[internalMountRadius,0,0],rotation=0);
                    screw_head(location=[0,internalMountRadius,0],rotation=-90);
                    screw_head(location=[-internalMountRadius,0,0],rotation=180);
                    screw_head(location=[0,-internalMountRadius,0],rotation=90);
                }
            }
        }
    }
}

projection(cut=false){
base_plate();
}

