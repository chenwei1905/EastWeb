import React from 'react'
import DustBin from './DustBin'
import Box from './Box'
const rowStyle = { overflow: 'hidden', clear: 'both' }
const Container = () => (
  <div>
    <div style={rowStyle}>
      <DustBin />
    </div>
    <div style={rowStyle}>
      <Box name="Glass" />
      <Box name="Banana" />
      <Box name="Paper" />
    </div>
  </div>
)
export default Container