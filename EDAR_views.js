








{{extend 'layout.html'}}
<!DOCTYPE HTML>
<html>
     <head>
 <meta http-equiv="X-UA-Compatible" content="IE=edge">

  <style>

  .estilotextarea
  {
  text-align: center;
  font-size: xx-large;
  font-weight: 900;
  position:relative;
  bottom: 43%;
  left:77%;
  width:70px;
  height:40px;
  border: 1px dotted #000099;
  }
 </style>
 </head>

	<div id=papel style="width: 1500px; height: 600px; top: 1000">
        <!--<input id="Velocidad" type="text" >-->
        <textarea id="Velocidad" class=estilotextarea></textarea>
        <audio id="Sonido" src="{{=URL('static','nautical021.mp3')}}"></audio>
    </div>

  <?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->


<script language="javascript">



  var estado2={'estado_ant': 0};
  var estado3={'estado_ant': 0};
  function enviodatos() {
        var datos={'operando1':  jQuery("#Velocidad").val()};

        jQuery.post("{{=URL('default','recibe_datos.json')}}", datos, {contentType: 'application/json'} )
              .success(function(datos_recibidos) {
                  jQuery("#resultado").html(datos_recibidos);

        });
  };




  jQuery(document).ready(function() {

	  angle = 0;
	  angle2 = 0;

      temp4=window.setInterval(function(){
		  jQuery.post("{{=URL('default','recogida_datos2.json')}}", estado2, {contentType: 'application/json'} )
			    .success(function(datos_recibidos) {

					/*Si llega 1500 no debemos de hacer nada ya que quiere decir que se ha leido el txt en mal momento*/
					console.log("Post realizado bien",datos_recibidos["valores"]);
					if(datos_recibidos["valores"]<100000){
						  /*console.log("Entra en el IF");*/
						  valor_aux=28000-datos_recibidos["valores"]
						  rect5.animate({height:(valor_aux/133)+10,y: 610-(valor_aux/133)},5000)
						}



				})
		  },3000);

      temp5=window.setInterval(function(){
		  jQuery.post("{{=URL('default','prueba_conexion.json')}}", estado2, {contentType: 'application/json'} )
			    .success(function(datos_recibidos) {
					if(datos_recibidos["valor"]==0){
						error_conexion.attr({fill : "black"});

						}
					if(datos_recibidos["valor"]==1){
									var anim31 = Raphael.animation({fill : "black"},100);
									error_conexion.animate(anim31.delay(2000));
									var anim32 = Raphael.animation({fill : "red"},100);
									error_conexion.animate(anim32.delay(1000));
									var a = document.getElementById("Sonido");
									a.play();

						}



				})
		  },3000);

      temp2=window.setInterval(function(){
		  jQuery.post("{{=URL('default','recogida_datos.json')}}", estado2, {contentType: 'application/json'} )
			    .success(function(datos_recibidos) {

					/*Si llega 1500 no debemos de hacer nada ya que quiere decir que se ha leido el txt en mal momento*/
					console.log("Post realizado bien",datos_recibidos["valores"]);
					if(datos_recibidos["valores"]<100000){
						  /*console.log("Entra en el IF");*/
						  rect4.animate({height:(datos_recibidos["valores"]/150)+10, y: 610-(datos_recibidos["valores"]/150)},5000)
						}



				})
		  },3000);


      temp3=window.setInterval(function(){
		  jQuery.post("{{=URL('default','recogida_salidas.json')}}", estado3, {contentType: 'application/json'} )
			    .success(function(datos_recibidos) {
						if(datos_recibidos["s3"]<100000){
								if(datos_recibidos["s3"]==1){
									s3.attr({fill : "#00FF00"})
									}
								if(datos_recibidos["s3"]==0){
									s3.attr({fill : "black"})
									}


            					if(datos_recibidos["al_gener_plc"]==0){
            						error_conexion.attr({fill : "black"});

            						}
            					if(datos_recibidos["al_gener_plc"]==1){
            									var anim33 = Raphael.animation({fill : "black"},100);
            									al_gener_plc.animate(anim33.delay(2000));
            									var anim34 = Raphael.animation({fill : "red"},100);
            									al_gener_plc.animate(anim34.delay(1000));
            									var a = document.getElementById("Sonido");
            									a.play();

            						}
								if(datos_recibidos["biodisco1"]==1){
									biodisco1.attr({opacity : 0.5})
									}
								if(datos_recibidos["biodisco1"]==0){
									biodisco1.attr({opacity : 0.1})
									}
								if(datos_recibidos["biodisco2"]==1){
									biodisco2.attr({opacity : 0.5})
									}
								if(datos_recibidos["biodisco2"]==0){
									biodisco2.attr({opacity : 0.1})
									}
								if(datos_recibidos["biodisco3"]==1){
									biodisco3.attr({opacity : 0.5})
									}
								if(datos_recibidos["biodisco3"]==0){
									biodisco3.attr({opacity : 0.1})
									}
								if(datos_recibidos["alarm_vent"]==0){
									alarm_vent.attr({opacity : 0})
									}
								if(datos_recibidos["alarm_vent"]==1){
									/*alarm_vent.attr({opacity : 0.5})*/
									var anim = Raphael.animation({opacity : 0},100);
									alarm_vent.animate(anim.delay(2000));
									var anim2 = Raphael.animation({opacity : 0.4},100);
									alarm_vent.animate(anim2.delay(1000));
									}

								if(datos_recibidos["alarm_desbaste"]==0){
									alarm_desbaste.attr({opacity : 0.1})
									}
								if(datos_recibidos["alarm_desbaste"]==1){

									var anim3 = Raphael.animation({opacity : 0.1},100);
									alarm_desbaste.animate(anim3.delay(2000));
									var anim4 = Raphael.animation({opacity : 0.9},100);
									alarm_desbaste.animate(anim4.delay(1000));
									}
								if(datos_recibidos["alarm_tamices"]==0){
									alarm_tamices.attr({opacity : 0.1})
									}
								if(datos_recibidos["alarm_tamices"]==1){

									var anim5 = Raphael.animation({opacity : 0.1},100);
									alarm_tamices.animate(anim5.delay(2000));
									var anim6 = Raphael.animation({opacity : 0.9},100);
									alarm_tamices.animate(anim6.delay(1000));
									}
								if(datos_recibidos["alarm_soplantes"]==0){
									alarm_soplantes.attr({opacity : 0.1})
									}
								if(datos_recibidos["alarm_soplantes"]==1){

									var anim7 = Raphael.animation({opacity : 0.1},100);
									alarm_soplantes.animate(anim7.delay(2000));
									var anim8 = Raphael.animation({opacity : 0.9},100);
									alarm_soplantes.animate(anim8.delay(1000));
									}
								if(datos_recibidos["al_rec_solidos"]==0){
									al_rec_solidos.attr({opacity : 0.1})
									}
								if(datos_recibidos["al_rec_solidos"]==1){

									var anim9 = Raphael.animation({opacity : 0.1},100);
									al_rec_solidos.animate(anim9.delay(2000));
									var anim10 = Raphael.animation({opacity : 0.9},100);
									al_rec_solidos.animate(anim10.delay(1000));
									}
								if(datos_recibidos["alarm_biodiscos"]==0){
									alarm_biodiscos.attr({opacity : 0.1})
									}
								if(datos_recibidos["alarm_biodiscos"]==1){

									var anim11 = Raphael.animation({opacity : 0.1},100);
									alarm_biodiscos.animate(anim11.delay(2000));
									var anim12 = Raphael.animation({opacity : 0.9},100);
									alarm_biodiscos.animate(anim12.delay(1000));
									}
								if(datos_recibidos["al_rec_grasas"]==0){
									al_rec_grasas.attr({opacity : 0.1})
									}
								if(datos_recibidos["al_rec_grasas"]==1){

									var anim13 = Raphael.animation({opacity : 0.1},100);
									al_rec_grasas.animate(anim13.delay(2000));
									var anim14 = Raphael.animation({opacity : 0.9},100);
									al_rec_grasas.animate(anim14.delay(1000));
									}
								if(datos_recibidos["alarm_obst_extr"]==0){
									alarm_obst_extr.attr({opacity : 0.1})
									}
								if(datos_recibidos["alarm_obst_extr"]==1){

									var anim15 = Raphael.animation({opacity : 0.1},100);
									alarm_obst_extr.animate(anim15.delay(2000));
									var anim16 = Raphael.animation({opacity : 0.5},100);
									alarm_obst_extr.animate(anim16.delay(1000));
									}
								if(datos_recibidos["alarm_decantador"]==0){
									alarm_decantador.attr({opacity : 0.1})
									}
								if(datos_recibidos["alarm_decantador"]==1){

									var anim17 = Raphael.animation({opacity : 0.1},100);
									alarm_decantador.animate(anim17.delay(2000));
									var anim18 = Raphael.animation({opacity : 0.9},100);
									alarm_decantador.animate(anim18.delay(1000));
									}
								if(datos_recibidos["pas_agua_tanque"]==0){
									pas_agua_tanque.attr({opacity : 0.1})
									}
								if(datos_recibidos["pas_agua_tanque"]==1){

									var anim19 = Raphael.animation({opacity : 0.1},100);
									pas_agua_tanque.animate(anim19.delay(2000));
									var anim20 = Raphael.animation({opacity : 0.9},100);
									pas_agua_tanque.animate(anim20.delay(1000));
									}
								if(datos_recibidos["out_bivalva"]==0){
									out_bivalva.attr({opacity : 0.1});
									out_bivalva_2.attr({opacity : 0.1});
									rect6.animate({height:11},8000);
									img4.animate({y:14},8000);
									out_bivalva_2.animate({y:21},8000);
									}
								if(datos_recibidos["out_bivalva"]==1){

									var anim21 = Raphael.animation({opacity : 0.1},100);
									out_bivalva.animate(anim21.delay(2000));
									var anim22 = Raphael.animation({opacity : 0.9},100);
									out_bivalva.animate(anim22.delay(1000));
									var anim31 = Raphael.animation({opacity : 0.1},100);
									out_bivalva_2.animate(anim31.delay(2000));
									var anim32 = Raphael.animation({opacity : 0.9},100);
									out_bivalva_2.animate(anim32.delay(1000));
									rect6.animate({height:60},8000);
									img4.animate({y:69},8000);
									out_bivalva_2.animate({y:86},8000);
									}

								if(datos_recibidos["nivel_max_p_gruesos"]==0){
									nivel_max_p_gruesos.attr({opacity : 0.1});
									}
								if(datos_recibidos["nivel_max_p_gruesos"]==1){

									var anim23 = Raphael.animation({opacity : 0.1},100);
									nivel_max_p_gruesos.animate(anim23.delay(2000));
									var anim24 = Raphael.animation({opacity : 0.9},100);
									nivel_max_p_gruesos.animate(anim24.delay(1000));
									}
								if(datos_recibidos["al_obstr_bomba"]==0){
									al_obstr_bomba.attr({opacity : 0})
									}
								if(datos_recibidos["al_obstr_bomba"]==1){

									var anim25 = Raphael.animation({opacity : 0},100);
									al_obstr_bomba.animate(anim25.delay(2000));
									var anim26 = Raphael.animation({opacity : 0.4},100);
									al_obstr_bomba.animate(anim26.delay(1000));
									}
								if(datos_recibidos["soplantes"]==1){
									soplantes.attr({opacity : 0.9})
									}
								if(datos_recibidos["soplantes"]==0){
									soplantes.attr({opacity : 0.1})
									}
								if(datos_recibidos["alarm_fangos"]==0){
									alarm_fangos.attr({opacity : 0.1})
									}
								if(datos_recibidos["alarm_fangos"]==1){

									var anim27 = Raphael.animation({opacity : 0.1},100);
									alarm_fangos.animate(anim27.delay(2000));
									var anim28 = Raphael.animation({opacity : 0.9},100);
									alarm_fangos.animate(anim28.delay(1000));
									}
								if(datos_recibidos["bomba_extraccion"]==1){
									bomba_extraccion.attr({fill : "#00FF00"})
									}
								if(datos_recibidos["bomba_extraccion"]==0){
									bomba_extraccion.attr({fill : "black"})
									}
								if(datos_recibidos["motor_decantador"]==0){
									motor_decantador.attr({opacity : 0})
									}
								if(datos_recibidos["motor_decantador"]==1){

									var anim29 = Raphael.animation({opacity : 0},100);
									motor_decantador.animate(anim29.delay(2000));
									var anim30 = Raphael.animation({opacity : 0.4},100);
									motor_decantador.animate(anim30.delay(1000));
									}
								if(datos_recibidos["bomba_fangos"]==1){
									bomba_fangos.attr({fill : "#00FF00"})
									}
								if(datos_recibidos["bomba_fangos"]==0){
									bomba_fangos.attr({fill : "black"})
									}


						}




				})
		  },3000);



     temp4=window.setInterval(function(){
		  jQuery.post("{{=URL('default','recogida_entradas.json')}}", estado3, {contentType: 'application/json'} )
			    .success(function(datos_recibidos) {
						if(datos_recibidos["p1"]<100000){
								if(datos_recibidos["p1"]==1){
									P1.attr({fill : "#00FF00"})
									}
								if(datos_recibidos["p1"]==0){
									P1.attr({fill : "black"})
									}
								if(datos_recibidos["p2"]==1){
									P2.attr({fill : "#00FF00"})
									}
								if(datos_recibidos["p2"]==0){
									P2.attr({fill : "black"})
									}
								if(datos_recibidos["s1"]==1){
									s1.attr({fill : "#00FF00"})
									}
								if(datos_recibidos["s1"]==0){
									s1.attr({fill : "black"})
									}
								if(datos_recibidos["s4"]==1){
									s4.attr({fill : "#00FF00"})
									}
								if(datos_recibidos["s4"]==0){
									s4.attr({fill : "black"})
									}
								if(datos_recibidos["s5"]==1){
									s5.attr({fill : "#00FF00"})
									}
								if(datos_recibidos["s5"]==0){
									s5.attr({fill : "black"})
									}
								if(datos_recibidos["s6"]==1){
									s6.attr({fill : "#00FF00"})
									}
								if(datos_recibidos["s6"]==0){
									s6.attr({fill : "black"})
									}
								if(datos_recibidos["s7"]==1){
									s7.attr({fill : "#00FF00"})
									}
								if(datos_recibidos["s7"]==0){
									s7.attr({fill : "black"})
									}
								if(datos_recibidos["s8"]==1){
									s8.attr({fill : "#00FF00"})
									}
								if(datos_recibidos["s8"]==0){
									s8.attr({fill : "black"})
									}
								if(datos_recibidos["s9"]==1){
									s9.attr({fill : "#00FF00"})
									}
								if(datos_recibidos["s9"]==0){
									s9.attr({fill : "black"})
									}
								if(datos_recibidos["s10"]==1){
									s10.attr({fill : "#00FF00"})
									}
								if(datos_recibidos["s10"]==0){
									s10.attr({fill : "black"})
									}
								if(datos_recibidos["cuch_bivalva"]==1){
									cuch_bivalva.attr({fill : "#00FF00"})
									}
								if(datos_recibidos["cuch_bivalva"]==0){
									cuch_bivalva.attr({fill : "black"})
									}
								if(datos_recibidos["s11"]==1){
									s11.attr({fill : "#00FF00"})
									}
								if(datos_recibidos["s11"]==0){
									s11.attr({fill : "black"})
									}
								if(datos_recibidos["s12"]==1){
									s12.attr({fill : "#00FF00"})
									}
								if(datos_recibidos["s12"]==0){
									s12.attr({fill : "black"})
									}
								if(datos_recibidos["s13"]==1){
									s13.attr({fill : "#00FF00"})
									}
								if(datos_recibidos["s13"]==0){
									s13.attr({fill : "black"})
									}
								if(datos_recibidos["act_ventiladores"]==1){
									act_ventiladores.attr({fill : "#00FF00"})
									angle-=1400;
									    if(datos_recibidos["s14"]==0){
											img.animate({
											transform: "r" + angle
											},3000,">");
											}
										if(datos_recibidos["s15"]==0){
											img2.animate({
											transform: "r" + angle
											},3000,">");
											}
									}
								if(datos_recibidos["act_ventiladores"]==0){
									act_ventiladores.attr({fill : "black"})
									}
								if(datos_recibidos["s14"]==1){
									s14.attr({fill : "#FF0000"})
									}
								if(datos_recibidos["s14"]==0){
									s14.attr({fill : "black"})
									}
								if(datos_recibidos["s15"]==1){
									s15.attr({fill : "#FF0000"})
									}
								if(datos_recibidos["s15"]==0){
									s15.attr({fill : "black"})
									}
								if(datos_recibidos["s16"]==1){
									s16.attr({fill : "#00FF00"})
									}
								if(datos_recibidos["s16"]==0){
									s16.attr({fill : "black"})
									}

								/*if(datos_recibidos["orden_soplantes"]==1){
									orden_soplantes.attr({fill : "#00FF00"})
									}
								if(datos_recibidos["orden_soplantes"]==0){
									orden_soplantes.attr({fill : "black"})
									}*/
								if(datos_recibidos["s17"]==1){
									s17.attr({fill : "#FF0000"})
									}
								if(datos_recibidos["s17"]==0){
									s17.attr({fill : "black"})
									}
								if(datos_recibidos["s19"]==1){
									s19.attr({fill : "#00FF00"})
									}
								if(datos_recibidos["s19"]==0){
									s19.attr({fill : "black"})
									}
								if(datos_recibidos["s20"]==1){
									s20.attr({fill : "#00FF00"})
									}
								if(datos_recibidos["s20"]==0){
									s20.attr({fill : "black"})
									}
								if(datos_recibidos["s22"]==1){
									s22.attr({fill : "#FF0000"})
									}
								if(datos_recibidos["s22"]==0){
									s22.attr({fill : "black"})
									}
								if(datos_recibidos["s23"]==1){
									s23.attr({fill : "#FF0000"})
									}
								if(datos_recibidos["s23"]==0){
									s23.attr({fill : "black"})
									}
								if(datos_recibidos["s24"]==1){
									s24.attr({fill : "#FF0000"})
									}
								if(datos_recibidos["s24"]==0){
									s24.attr({fill : "black"})
									}
								if(datos_recibidos["s25"]==1){
									s25.attr({fill : "#00FF00"})
									}
								if(datos_recibidos["s25"]==0){
									s25.attr({fill : "black"})
									}
								if(datos_recibidos["act_biodiscos"]==1){
									act_biodiscos.attr({fill : "#00FF00"})
									}
								if(datos_recibidos["act_biodiscos"]==0){
									act_biodiscos.attr({fill : "black"})
									}
								if(datos_recibidos["s26"]==1){
									s26.attr({fill : "#00FF00"})
									}
								if(datos_recibidos["s26"]==0){
									s26.attr({fill : "black"})
									}


						}




				})
		  },2000);


	var src = document.getElementById("ventilador").src;

	var src2 = document.getElementById("ventilador2").src;
	var src3 = document.getElementById("pala").src;
	var src4 = document.getElementById("pala1").src;
	var src5 = document.getElementById("edar").src;


	/*var	paper = Raphael(130, 450, 1500,1000);*/
	/*var	paper = Raphael(150, 450, 1500,1000);*/
	var paper =  Raphael("papel");
	/*paper.setViewBox(100,0,1500,800,true)*/

	/*paper.setViewBox(-100,-400,1500,800,true);
	paper.canvas.setAttribute('preserveAspectRatio','none');*/




	var img = paper.image(src,915,12,25,25);
	var img2 = paper.image(src2,975,12,25,25);
	var img5 = paper.image(src5,67,-55,1055,750);




	var img3 = paper.image(src3,557,0,20,20);

		var rect6= paper.rect(564,9,5,11)
		.attr({
			fill : "black",
			stroke : "none",
			opacity : 1
			})
	var img4 = paper.image(src4,555,14,22,20);


	var rect4= paper.rect(665,610,90,10)
		.attr({
			fill : "blue",
			stroke : "none",
			opacity : 0.5
			})

	var rect5= paper.rect(900,610,90,10)
		.attr({
			fill : "black",
			stroke : "none",
			opacity : 0.5
			})

	var control= paper.rect(1105,49,258,275)
		.attr({
			fill : "#B0C4DE",
			"stroke-width" : 8,
			opacity : 1
			})

	var control2= paper.rect(1120,9,231,40)
		.attr({
			fill : "#F4A460",
			"stroke-width" : 5,
			opacity : 1
			})

	var enviar_velocidad= paper.rect(1245,347,170,50)
		.attr({
			fill : "#4972B5",
			"stroke-width" : 2,
			opacity : 1
			})
		.click(function(){
		    enviodatos();
		    })

	  /*paper.text(1330,410,"Enviar Velocidad")
		.attr({
			"font-size" : 15,
			"font-weight" : "800",
			fill: "black",
			"font-family" : "Verdana",
			})*/

	  paper.text(1117,370,"1-9")
		.attr({
			"font-size" : 32,
			"font-weight" : "800",
			stroke: "#4972B5",
			"font-family" : "Verdana",
			})

	  paper.text(1235,25,"PANEL DE CONTROL")
		.attr({
			"font-size" : 21,
			"font-family" : "Georgia"
			})

	  paper.text(60,25,"MARCHA")
		.attr({
			"font-size" : 18,
			"font-family" : "Georgia"
			})

	  paper.text(60,130,"PARO")
		.attr({
			"font-size" : 18,
			"font-family" : "Georgia"
			})

	  paper.text(1240,155,"ALARMA PLC")
		.attr({
			"font-size" : 18,
			"font-family" : "Georgia"
			})

	  paper.text(1253,225,"ACT. BIODISCOS")
		.attr({
			"font-size" : 18,
			"font-family" : "Georgia"
			})

	  paper.text(1270,295,"BOMBA DE FANGOS")
		.attr({
			"font-size" : 18,
			"font-family" : "Georgia"
			})

	  paper.text(447,577,"DECANTADOR LLENO")
		.attr({
			"font-size" : 13,
			"font-family" : "Georgia"
			})

	  paper.text(545,162,"NIVEL MAX")
		.attr({
			"font-size" : 10,
			"font-family" : "Georgia"
			})

	  paper.text(432,610,"ALARMA FANGOS")
		.attr({
			"font-size" : 13,
			"font-family" : "Georgia"
			})

	  paper.text(1270,85,"ERROR CONEXION")
		.attr({
			"font-size" : 18,
			"font-family" : "Georgia"
			})

	  var s3 = paper.circle(382,60,5,5)
		.attr({
			fill : "black"
			})

	  var pas_agua_tanque = paper.circle(215,75,8,8)
		.attr({
			fill : "#00FF00",
			opacity : 0.1,
			"stroke-width" : 5
			})

	  var error_conexion = paper.circle(1140,85,20,20)
		.attr({
			fill : "black"
			})

	  var al_gener_plc = paper.circle(1140,155,20,20)
		.attr({
			fill : "black"
			})

	  var out_bivalva = paper.circle(502,30,6,6)
		.attr({
			fill : "#00FF00",
			opacity : 0.1,
			"stroke-width" : 3
			})

	  var out_bivalva_2 = paper.circle(566,21,3,3)
		.attr({
			fill : "red",
			opacity : 0.1,
			})

	  var biodisco1 = paper.rect(334,247,65,105)
		.attr({
			fill : "green",
			opacity : 0.1
			})

	  var biodisco2 = paper.rect(244,247,40,102)
		.attr({
			fill : "green",
			opacity : 0.1
			})

	  var biodisco3 = paper.rect(154,247,40,102)
		.attr({
			fill : "green",
			opacity : 0.1
			})

	  var alarm_vent = paper.rect(880,0,155,65)
		.attr({
			fill : "red",
			opacity : 0
			})

	  var alarm_desbaste = paper.circle(682,135,8,8)
		.attr({
			fill : "red",
			opacity : 0.1,
			"stroke-width" : 5
			})

	  var alarm_tamices = paper.circle(970,135,8,8)
		.attr({
			fill : "red",
			opacity : 0.1,
			"stroke-width" : 5
			})

	  var alarm_soplantes = paper.circle(1015,225,8,8)
		.attr({
			fill : "red",
			opacity : 0.1,
			"stroke-width" : 5
			})

	  var al_rec_solidos = paper.circle(773,190,5,5)
		.attr({
			fill : "red",
			opacity : 0.1,
			"stroke-width" : 2
			})

	  var alarm_biodiscos = paper.circle(270,407,8,8)
		.attr({
			fill : "red",
			opacity : 0.1,
			"stroke-width" : 5
			})

	  var al_rec_grasas = paper.circle(447,253,5,5)
		.attr({
			fill : "red",
			opacity : 0.1,
			"stroke-width" : 2
			})

	  var alarm_obst_extr = paper.rect(685,295,260,65)
		.attr({
			fill : "red",
			opacity : 0
			})

	  var alarm_decantador = paper.circle(350,575,10,10)
		.attr({
			fill : "red",
			opacity : 0.1,
			"stroke-width" : 5
			})

	  var nivel_max_p_gruesos = paper.circle(497,162,8,8)
		.attr({
			fill : "red",
			opacity : 0.1,
			"stroke-width" : 5
			})

	  var al_obstr_bomba = paper.rect(322,123,77,54)
		.attr({
			fill : "red",
			opacity : 0
			})

	  var soplantes = paper.circle(947,225,8,8)
		.attr({
			fill : "#00FF00",
			opacity : 0.1,
			"stroke-width" : 5
			})

	  var alarm_fangos = paper.circle(350,610,10,10)
		.attr({
			fill : "red",
			opacity : 0.1,
			"stroke-width" : 5
			})

	  var motor_decantador = paper.rect(310,460,23,25)
		.attr({
			fill : "#00FF00",
			opacity : 0
			})

	  var bomba_fangos = paper.circle(1140,295,20,20)
		.attr({
			fill : "black"
			})

		/*A partir de aqui ENTRADAS*/
		/*CANAL 0*/
	  var P1 = paper.circle(65,65,20,20)
		.attr({
			fill : "black",
			"stroke-width" : 5
			})

	  var P2 = paper.circle(62,175,20,20)
		.attr({
			fill : "black",
			"stroke-width" : 5
			})

	  var s1 = paper.circle(310,40,5,5)
		.attr({
			fill : "black"
			})

	  var s4 = paper.circle(364,85,5,5)
		.attr({
			fill : "black"
			})

	  var s5 = paper.circle(260,150,5,5)
		.attr({
			fill : "black"
			})

	  var s6 = paper.circle(260,130,5,5)
		.attr({
			fill : "black"
			})

	  var s7 = paper.circle(353,139,5,5)
		.attr({
			fill : "black"
			})

	  var s8 = paper.circle(364,105,5,5)
		.attr({
			fill : "black"
			})

		/*CANAL 1*/
	  var s9 = paper.circle(460,80,5,5)
		.attr({
			fill : "black"
			})

	  var s10 = paper.circle(502,104,5,5)
		.attr({
			fill : "black"
			})

	  var cuch_bivalva = paper.circle(502,10,5,5)
		.attr({
			fill : "black"
			})

	  var s11 = paper.circle(642,75,5,5)
		.attr({
			fill : "black"
			})

	  var s12 = paper.circle(865,95,5,5)
		.attr({
			fill : "black"
			})

	  var s13 = paper.circle(1050,95,5,5)
		.attr({
			fill : "black"
			})

		/*CANAL 2*/
	  var act_ventiladores = paper.circle(958,42,8,8)
		.attr({
			fill : "black"
			})

	  var s14 = paper.circle(895,37,5,5)
		.attr({
			fill : "black"
			})

	  var s15 = paper.circle(1020,37,5,5)
		.attr({
			fill : "black"
			})

	  var s16 = paper.circle(843,150,5,5)
		.attr({
			fill : "black"
			})

	  var s17 = paper.circle(933,257,5,5)
		.attr({
			fill : "black"
			})

	  var s18 = paper.circle(985,323,5,5)
		.attr({
			fill : "black"
			})

	  var s19 = paper.circle(804,252,5,5)
		.attr({
			fill : "black"
			})

		/*CANAL 3*/
	  var s20 = paper.circle(644,266,5,5)
		.attr({
			fill : "black"
			})

	  var s22 = paper.circle(310,250,5,5)
		.attr({
			fill : "black"
			})

	  var s23 = paper.circle(221,250,5,5)
		.attr({
			fill : "black"
			})

	  var s24 = paper.circle(133,250,5,5)
		.attr({
			fill : "black"
			})

	  var s25 = paper.circle(514,470,5,5)
		.attr({
			fill : "black"
			})

	  var act_biodiscos = paper.circle(1140,225,20,20)
		.attr({
			fill : "black"
			})

		/*CANAL 4*/
	  var s26 = paper.circle(275,525,5,5)
		.attr({
			fill : "black"
			})

  });


</script>
<body>
		<div id="holder">
            <img id="ventilador" src="{{=URL('static','ventilador.jpg')}}" width="0" height="0">
            <img id="ventilador2" src="{{=URL('static','ventilador2.jpg')}}" width="0" height="0">
            <img id="pala" src="{{=URL('static','pala.jpeg')}}" width="0" height="0">
            <img id="pala1" src="{{=URL('static','pala1.jpeg')}}" width="0" height="0">
            <img id="edar" src="{{=URL('static','edarbuena.svg')}}" width="0" height="0">
        </div>



</body>
</html>


