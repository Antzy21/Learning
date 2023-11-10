%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  Author: Barrie Cooper.        %%
%%  This file created 10/11/2008  %%
%%  as a selection of material    %%
%%  from older files.             %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

beginfig(1);
    numeric scf, unit;
    scf=1; unit=scf*0.5in;

    pickup pencircle scaled scf;

    pair v[];

    v1=(0,0); v3-v1=unit*dir(30); v4-v1=unit*dir(150); v2-v1=1.5*unit*dir(90);
    draw v2--v1; draw v2--v4; draw v2--v3;
    draw v1{dir 60}..{dir 0}v3; draw v1{dir 0}..{dir 60}v3;
    draw v1{dir 120}..{dir 180}v4; draw v1{dir 180}..{dir 120}v4;

    pickup pencircle scaled 4;
    draw v1 withcolor red; draw v2 withcolor red; draw v3 withcolor red; draw v4 withcolor red;
    
    label.bot(btex $1$ etex, v1);
    label.top(btex $2$ etex, v2);
    label.rt(btex $3$ etex, v3);
    label.lft(btex $4$ etex, v4);
endfig;

beginfig(2);
    numeric scf, unit;
    scf=1; unit=scf*0.5in;

    pickup pencircle scaled scf;

    pair v[];

    v1=(0,0); v3-v1=unit*dir(30); v4-v1=unit*dir(150); v2-v1=1.5*unit*dir(90);
    draw v2--v1 withcolor red; draw v2--v3 withcolor red;
    draw v1{dir 60}..{dir 0}v3 withcolor red; draw v1{dir 0}..{dir 60}v3 withcolor red;
    draw v1--v4 withcolor red;

    draw fullcircle scaled (0.5*unit) shifted (0.25*unit,0) rotated 150 shifted v4 withcolor red;

    v5-v3=0.5*unit*dir(0); v6-v5=unit*dir(80);
    draw v5{dir 50}..{dir 110}v6 withcolor red; draw v5{dir 110}..{dir 50}v6 withcolor red;

    pickup pencircle scaled 4;
    draw v1; draw v2; draw v3; draw v4; draw v5; draw v6;
endfig;

beginfig(3);
    pair a[][], o;
    numeric scf, unit;
    
    scf=0.5; unit=scf*1in;
    pickup pencircle scaled (0.2*scf);
        
    o=(0,0); a[1][0]-o=unit*dir(90); a[1][1]-o=unit*dir(-30);
    
    numeric length;
    length=1;
    numeric iterates;
    iterates=6;
    
    for i=2 upto iterates:
    for j=0 upto (length-1):
        a[i][4*j]=a[i-1][j];
        a[i][4*j+4]=a[i-1][j+1];
        a[i][4*j+1]=(1/3)[a[i][4*j],a[i][4*j+4]];
        a[i][4*j+3]=(2/3)[a[i][4*j],a[i][4*j+4]];
        a[i][4*j+2]=point 10 of ((a[i][4*j+1]--a[i][4*j+3]) shifted (o-a[i][4*j+1]) rotated 60 shifted a[i][4*j+1]);
    endfor;
    length:=length*4;
    endfor;
    
    path p[];
    p1=a[iterates][0];
    
    for k=1 upto length:
        p1:=p1--a[iterates][k];
    endfor;
        
    p2=p1 rotated 240;
    p3=p1 rotated 120;
    p4=p1--p2--p3--cycle;
    draw p4;
    
    pair b[][];
    numeric lilunit;
    lilunit=0.9*unit;
    
    b[1][0]-o=lilunit*dir(90); b[1][1]-o=lilunit*dir(-30);
    
    numeric blength;
    blength=1;
    numeric biterates;
    biterates=6;
    
    for i=2 upto biterates:
    for j=0 upto (blength-1):
        b[i][4*j]=b[i-1][j];
        b[i][4*j+4]=b[i-1][j+1];
        b[i][4*j+1]=(1/3)[b[i][4*j],b[i][4*j+4]];
        b[i][4*j+3]=(2/3)[b[i][4*j],b[i][4*j+4]];
        b[i][4*j+2]=point 10 of ((b[i][4*j+1]--b[i][4*j+3]) shifted (o-b[i][4*j+1]) rotated (-60) shifted b[i][4*j+1]);
    endfor;
    blength:=blength*4;
    endfor;
    
    p11=b[biterates][0];
    
    for k=1 upto (length/2):
        p11:=p11--b[biterates][k];
    endfor;
    
    p12=p11 shifted (o-b[biterates][0]) rotated 120;    
    p21=p11--p12;
    p22=p21 rotated 300;
    p23=p21 rotated 240;
    p24=p21 rotated 180;
    p25=p21 rotated 120;
    p26=p21 rotated 60;
    p27=p21--p22--p23--p24--p25--p26--cycle;
    
    fill (p4--(reverse p27)--cycle) withcolor black;
    draw p27;
endfig;

end
