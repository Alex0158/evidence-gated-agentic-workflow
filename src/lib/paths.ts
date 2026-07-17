const base = import.meta.env.BASE_URL.replace(/\/$/, '');

export function pathFor(path = '/') {
  if (/^https?:\/\//.test(path)) return path;
  const normalized = path.startsWith('/') ? path : `/${path}`;
  return `${base}${normalized}`;
}
