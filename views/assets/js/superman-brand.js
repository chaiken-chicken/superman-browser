/* SUPERMAN BROWSER visual rebrand; no proxy internals or requests are intercepted. */
(() => {
  const rename = text => typeof text === 'string'
    ? text.replace(/InvisiProxy\s*LTS/gi,'SUPERMAN BROWSER')
          .replace(/InvisiProxy/gi,'SUPERMAN')
          .replace(/Holy Unblocker\s*LTS/gi,'SUPERMAN BROWSER')
    : text;
  const apply = root => {
    try {
      document.title = rename(document.title);
      const base = root.nodeType === 1 ? root : document.body;
      if (!base) return;
      if (base.closest && base.closest('code,pre,script,style,[data-no-rebrand]')) return;
      if (base.nodeType === 1) for (const a of ['title','alt','aria-label','placeholder']) {
        if (base.hasAttribute(a)) base.setAttribute(a,rename(base.getAttribute(a)));
      }
      const nodes=base.querySelectorAll ? base.querySelectorAll('[title],[alt],[aria-label],[placeholder]') : [];
      for (const el of nodes) {
        if (el.closest('code,pre,script,style,[data-no-rebrand]')) continue;
        for (const a of ['title','alt','aria-label','placeholder']) {
          if (el.hasAttribute(a)) {
            const prev=el.getAttribute(a),next=rename(prev);
            if (prev!==next)el.setAttribute(a,next);
          }
        }
      }
      // Keep original legal pages intact, but don't send ordinary visitors through
      // the upstream project's marketing links in the regular SUPERMAN interface.
      const promotions=base.querySelectorAll ? base.querySelectorAll('a[href]') : [];
      for (const anchor of promotions) {
        if (anchor.closest('[data-no-rebrand], .legal-notices, .license-notices')) continue;
        try {
          const dest=new URL(anchor.href, location.href);
          const oldSite=/(^|\.)invisiproxy\.com$/i.test(dest.hostname);
          const oldRepo=dest.hostname==='github.com'&&/^\/InvisiProxy\/InvisiProxyLTS(?:\/|$)/i.test(dest.pathname);
          if (!oldSite&&!oldRepo) continue;
          // The locally hosted Credits page continues to expose upstream attribution.
          anchor.setAttribute('href','/credits');
          if (!/(credits|attribution|license|source)/i.test(anchor.textContent||''))
            anchor.textContent='Credits';
        } catch (_) {}
      }
      const walker=document.createTreeWalker(base,NodeFilter.SHOW_TEXT);
      let n;while ((n=walker.nextNode())){
        if (n.parentElement?.closest('script,style,code,pre,[data-no-rebrand]')) continue;
        const text=rename(n.nodeValue);
        if (text!==n.nodeValue)n.nodeValue=text;
      }
    } catch(_){}
  };
  if (/\/(credits|license|privacy)(\/|$)/i.test(location.pathname)) return;
  let busy=false;
  const observer=new MutationObserver(() => {
    if(busy)return;busy=true;
    requestAnimationFrame(()=>{observer.disconnect();apply(document.body);observer.observe(document.body,{childList:true,subtree:true,characterData:true});busy=false;});
  });
  const init=()=>{
    apply(document.body);
    if(document.body)observer.observe(document.body,{childList:true,subtree:true,characterData:true});
    // Hide old site-branded hero images only when they were not replaced during build.
    // App and provider icons (TikTok, chess, etc.) are left untouched.
  };
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init,{once:true});
  else init();
})();
