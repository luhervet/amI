import { NextRequest, NextResponse } from 'next/server';
import { getRelations, createRelation } from '@/lib/store';

export async function GET() {
  return NextResponse.json(getRelations());
}

export async function POST(req: NextRequest) {
  const body = await req.json();
  const { fromId, toId, type, description, strength } = body;
  if (!fromId || !toId || !type || !strength) {
    return NextResponse.json({ error: 'Missing required fields' }, { status: 400 });
  }
  const relation = createRelation({ fromId, toId, type, description: description || '', strength });
  return NextResponse.json(relation, { status: 201 });
}
