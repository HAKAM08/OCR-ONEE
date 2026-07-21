export interface OCRResult {
  id: number;
  text: string;
  confidence: number;
  language: string;
  processing_time: number;
  page_count: number;
  document_id: number;
}