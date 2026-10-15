
const $=s=>document.querySelector(s),mb=$('#mb'),nv=$('#nv');
mb.onclick=()=>{const o=nv.classList.toggle('open');mb.setAttribute('aria-expanded',o)};
nv.querySelectorAll('a').forEach(a=>a.onclick=()=>{nv.classList.remove('open');mb.setAttribute('aria-expanded',false)});
document.onkeydown=e=>{if(e.key==='Escape'&&nv.classList.contains('open')){nv.classList.remove('open');mb.setAttribute('aria-expanded',false);mb.focus()}};
document.querySelectorAll('[data-s]').forEach(a=>a.addEventListener('click',()=>{$('#sv').value=a.dataset.s}));
const lb=$('#lb');let im=[],k=0;
const show=i=>{k=(i+im.length)%im.length;$('#li').src=im[k].src;$('#li').alt=im[k].alt;$('#lc').textContent=im[k].closest('figure').querySelector('figcaption').textContent+' · '+(k+1)+' de '+im.length};
document.querySelectorAll('[data-lb]').forEach(c=>c.querySelectorAll('img').forEach((x,i)=>x.parentNode.onclick=()=>{im=[...c.querySelectorAll('img')];show(i);lb.showModal()}));
$('#pv').onclick=()=>show(k-1);$('#nx').onclick=()=>show(k+1);$('#cl').onclick=()=>lb.close();
lb.addEventListener('click',e=>{if(e.target===lb)lb.close()});
lb.addEventListener('keydown',e=>{if(e.key==='ArrowLeft')show(k-1);if(e.key==='ArrowRight')show(k+1)});
const f=$('#cotizar'),sb=$('#sb'),st=$('#st'),d=$('#d');
const R={n:'Escriba su nombre.',t:'Escriba un teléfono de contacto.',sv:'Seleccione el servicio requerido.',d:'Describa brevemente el problema del motor.'};
const phoneOk=v=>/^[+\d][\d\s().-]*$/.test(v)&&v.replace(/\D/g,'').length>=8,mailOk=v=>/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v);
function chk(id){const el=$('#'+id),v=el.value.trim();let m='';
if(R[id]&&!v)m=R[id];else if(id==='t'&&v&&!phoneOk(v))m='Escriba un teléfono válido, con al menos 8 dígitos.';else if(id==='e'&&v&&!mailOk(v))m='Escriba un correo válido o deje el campo vacío.';
$('#'+id+'-e').textContent=m;el.setAttribute('aria-invalid',m?'true':'false');return m?el:null}
d.addEventListener('input',()=>$('#cnt').textContent=d.value.length+' / 1000');
['n','t','e','sv','d'].forEach(id=>$('#'+id).addEventListener('blur',()=>chk(id)));
f.addEventListener('submit',async e=>{e.preventDefault();if(f.dataset.busy)return;
const bad=['n','t','e','sv','d'].map(chk).filter(Boolean);
if(bad.length){bad[0].focus();st.className='bad';st.textContent='Revise los campos marcados antes de enviar.';return}
f.dataset.busy=1;sb.disabled=true;sb.textContent='Enviando…';st.className='';st.textContent='Enviando su solicitud…';
try{if(window.REMEG_PREVIEW)throw new Error('preview');
const r=await fetch('/',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:new URLSearchParams(new FormData(f))});
if(!r.ok)throw new Error(r.status);
track('form_enviado');f.reset();$('#cnt').textContent='0 / 1000';st.className='ok';st.textContent='Solicitud enviada. REMEG se pondrá en contacto con usted.';st.focus()}
catch(_){st.className='bad';st.textContent=window.REMEG_PREVIEW?'Vista previa: el envío real solo funciona en el sitio desplegado.':'No pudimos enviar su solicitud. Sus datos siguen en el formulario: intente de nuevo o contáctenos por teléfono (4726-4881 / 4715-4643) o WhatsApp.';st.focus()}
finally{delete f.dataset.busy;sb.disabled=false;sb.textContent='Enviar solicitud de cotización'}});

const uid=document.querySelector('meta[name="umami-website-id"]')?.content;
if(uid&&!window.REMEG_PREVIEW){const s=document.createElement('script');s.defer=true;s.src='https://cloud.umami.is/script.js';s.dataset.websiteId=uid;s.dataset.doNotTrack='true';document.head.appendChild(s)}
function track(n){try{window.umami&&window.umami.track(n)}catch(_){}}
document.addEventListener('click',e=>{const a=e.target.closest('a');if(!a)return;const u=a.getAttribute('href')||'';
if(u.startsWith('tel:'))track('click_llamar');else if(u.includes('wa.me'))track('click_whatsapp');else if(u.startsWith('mailto:'))track('click_correo');else if(u.includes('google.com/maps'))track('click_mapa')});
const waf=$('#waf');if(waf){const t=()=>waf.classList.toggle('show',scrollY>600);addEventListener('scroll',t,{passive:true});t()}
if(matchMedia('(hover:hover)').matches){const o=$('#steps');o.classList.add('hv');o.querySelectorAll('li').forEach(l=>l.tabIndex=0)}

const reduce=matchMedia('(prefers-reduced-motion:reduce)').matches,gm=$('#gm');
if(gm)gm.onclick=()=>{const o=gm.getAttribute('aria-expanded')==='true',n=document.querySelectorAll('#gal figure').length;document.querySelectorAll('#gal .more').forEach(f=>f.hidden=o);gm.setAttribute('aria-expanded',String(!o));gm.textContent=o?'Ver todas las fotos ('+n+')':'Ver menos fotos'};
document.querySelectorAll('.car').forEach(c=>{const t=c.querySelector('.track'),p=c.querySelector('.cp'),n=c.querySelector('.cn');
const step=()=>t.querySelector('figure').getBoundingClientRect().width+(parseFloat(getComputedStyle(t).columnGap)||16);
const upd=()=>{p.setAttribute('aria-disabled',String(t.scrollLeft<=2));n.setAttribute('aria-disabled',String(t.scrollLeft+t.clientWidth>=t.scrollWidth-2))};
const go=d=>{t.scrollBy({left:d*step(),behavior:reduce?'auto':'smooth'})};
p.onclick=()=>{if(p.getAttribute('aria-disabled')!=='true')go(-1)};n.onclick=()=>{if(n.getAttribute('aria-disabled')!=='true')go(1)};
t.addEventListener('scroll',upd,{passive:true});addEventListener('resize',upd);upd()});
