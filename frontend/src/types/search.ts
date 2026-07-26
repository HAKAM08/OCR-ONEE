export interface SearchResult {
  document_id: number;
  filename: string;
  confidence: number;
  page_count: number;
  score: number;
  highlights: string[];
}