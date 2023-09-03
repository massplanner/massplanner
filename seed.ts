import { db } from '@/lib/db'
import { type Occupation } from '@prisma/client'
import fs from 'fs'
import { openai } from '@/lib/openai'
import path from 'path'

import StandardOccupationsData from './data/standard-occupations.json'

if (!process.env.OPENAI_API_KEY) {
  throw new Error('process.env.OPENAI_API_KEY is not defined. Please set it.')
}

if (!process.env.POSTGRES_URL) {
  throw new Error('process.env.POSTGRES_URL is not defined. Please set it.')
}



async function main() {
  try {
    const seed = await db.occupations.findFirst({
      where: {
        title: 'Chief Executives',
      },
    })
    if (seed) {
      console.log('OccupationDex already seeded!')
      return
    }
  } catch (error) {
    console.error('Error checking if "Chief Executives" exists in the database.')
    throw error
  }
  for (const record of (StandardOccupationsData as any).data) {
    // In order to save time, we'll just use the embeddings we've already generated
    // for each Pokémon. If you want to generate them yourself, uncomment the
    // following line and comment out the line after it.

    const embedding = await generateEmbedding(record.soc_definition);
    await new Promise((r) => setTimeout(r, 500)); // Wait 500ms between requests;
    // const { embedding, ...p } = record

    // Create the pokemon in the database
    const occupation = await db.occupations.create({
      data: {
        title: record.soc_title,
        code: record.soc_code,
        definition: record.soc_definition,
        group: record.soc_group,
      },
    })

    // Add the embedding
    await db.$executeRaw`
        UPDATE occupation
        SET embedding = ${embedding}::vector
        WHERE id = ${occupation.id}
    `

    console.log(`Added ${occupation.title} ${occupation.code}`)
  }

  // Uncomment the following lines if you want to generate the JSON file
  // fs.writeFileSync(
  //   path.join(__dirname, "./embeddings/standard-occupations-with-embeddings.json"),
  //   JSON.stringify({ data }, null, 2),
  // );
  console.log('StandardOccupationDex seeded successfully!')
}
main()
  .then(async () => {
    await db.$disconnect()
  })
  .catch(async (e) => {
    console.error(e)
    await db.$disconnect()
    process.exit(1)
  })

async function generateEmbedding(_input: string) {
  const input = _input.replace(/\n/g, ' ')
  const embeddingResponse = await openai.createEmbedding({
    model: 'text-embedding-ada-002',
    input,
  })

  const embeddingData = await embeddingResponse.json()
  const [{ embedding }] = (embeddingData as any).data
  return embedding
}