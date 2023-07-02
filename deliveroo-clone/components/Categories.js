import React, { Component } from 'react'
import { ScrollView, Text, View } from 'react-native'
import CategoryCard from './CategoryCard'
import FeaturedRow from './FeaturedRow'

export class Categories extends Component {
  render() {
    return (
      <ScrollView 
      contentContainerStyle={{
        paddingHorizontal: 15,
        paddingTop: 10,
      }}
      horizontal>
        {/* Category Card */}
      <CategoryCard imgUrl="https://links.papareact.com/gn7" title="Testing" />
      <CategoryCard imgUrl="https://links.papareact.com/gn7" title="Testing"/>
      <CategoryCard imgUrl="https://links.papareact.com/gn7" title="Testing"/>
      <CategoryCard imgUrl="https://links.papareact.com/gn7" title="Testing"/>
      <CategoryCard imgUrl="https://links.papareact.com/gn7" title="Testing"/>


      </ScrollView>
    )
  }
}

export default Categories
