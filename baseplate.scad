$fa = 1;
$fs = 0.4;
standLocationRadius=56.0;
standRadius=2.5;
standHoleRadius=1.0;
standLipWidth=1.5;
standLipHeight=1.5;
standHeight=3.0;
standHoleDepth=5.0;

module screw_head(location=[0.0,0.0,0.0],rotation=0.0) {
    translate(location) {
 //       rotate([0,0,rotation]){
            cylinder(h=6,
                    r1=standRadius*2,
                    r2=standHoleRadius/2,
                    center=true);
 //       }
    }
}
difference(){
    cylinder(r=62,h=2,center=false);
    union(){
        translate([12,0,0]){
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
    }
}


