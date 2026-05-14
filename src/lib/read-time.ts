const WPM = 200;
const SECONDS_PER_BLOCK = 30;

export function computeReadTime(body: string, hasHero: boolean): number {
  const words = body.split(/\s+/).filter(Boolean).length;
  const codeBlocks = ((body.match(/^```/gm) ?? []).length / 2) | 0;
  const inlineImages = (body.match(/!\[/g) ?? []).length;
  const figures = inlineImages + (hasHero ? 1 : 0);
  const minutes = words / WPM + ((codeBlocks + figures) * SECONDS_PER_BLOCK) / 60;
  return Math.max(1, Math.ceil(minutes));
}
